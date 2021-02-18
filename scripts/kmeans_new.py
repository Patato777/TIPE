import configparser
import logging
import os
import time
import scripts.baseseeds as bs

from scripts.graph import *

dirname = os.path.dirname(__file__)
conf = configparser.ConfigParser()
conf.read(dirname + '/resources/config')
config = conf['kmeans']


class AgregGraph(Graph):  # Children class of Graph, for this specific algorithm
    def agreg(self, seeds):  # Aggregation of vertices around the seeds
        k = len(seeds)  # Number of clusters
        # Associating ids to the corresponding vertices
        seeds = [self.vertices[seed] for seed in seeds]
        # Creating k clusters, each containing a different seed
        self.pools = [Pool(i) for i in range(k)]
        for i in range(k):
            self.pools[i].vertices.append(seeds[i])
            self.pools[i].center = seeds[i]
            for vertex in self.vertices:
                if vertex.id != seeds[i].id:
                    del vertex.free_edges[seeds[i].id]  # TODO: Wa da fuk?
        # Adding one vertex to each cluster each time
        for augment in range(len(self.vertices) // k - 1):
            new_vertices = list()
            for pool in self.pools:
                logging.debug(str(pool.center.free_edges))  # debug
                # Adding the nearest vertex from the center of the pool
                free_vertices = [self.vertices[i] for i in pool.center.free_edges]
                pool.new_vertex = min(free_vertices, key=eval(f'pool.{config["DISTTOVERTEX"]}'))
                logging.debug(str([nod.id for nod in pool.vertices]))  # debug
                # Eliminating the connection to the other vertices
                for vertex in self.vertices:
                    try:
                        if vertex.id != pool.new_vertex.id:
                            del vertex.free_edges[pool.new_vertex.id]
                    except Exception as error:  # TODO: Why does it throw that f***g error
                        logging.debug(
                            f'error:{error}, vertex:{vertex.id}, new vertex:{pool.new_vertex.id}, vertex.free edges:{vertex.free_edges.keys()}, new_vertex.free edges:{pool.new_vertex.free_edges.keys()}')
                while pool.new_vertex in new_vertices:  # It probably shouldn't happen... (I think?)
                    # Anyway, if 2 clusters try to aggregate the same vertex
                    self.conflict(pool, pool.new_vertex.pool)
                    logging.debug("C'est une boucle infinie MDR")  # debug
                new_vertices.append(pool.new_vertex)
                pool.new_vertex.pool = pool
                pool.vertices.append(pool.new_vertex)
                pool.center = min(pool.vertices,
                                  key=lambda n: pool.dist_to_vertex(n))  # Re-defining the center of the pool

    def conflict(self, pool1, pool2):  # If 2 clusters try to aggregate the same vertex
        vertex = pool1.new_vertex
        pool = max((pool1, pool2), key=lambda p: p.dist_to_vertex(vertex))
        pool.new_vertex = min(self.vertices, key=eval(f'pool.{config["DISTTOVERTEX"]}'))

    def calc_dist(self):
        return sum([pool.weight() for pool in self.pools])


class Pool:  # Class of clusters
    def __init__(self, nb):
        self.center = None
        self.id = nb
        self.size = 0
        self.vertices = list()

    def dist_to_vertex(self, vertex):  # The distance to a vertex
        return sum([vertex.edges[pvertex.id].length for pvertex in self.vertices])

    def to_center(self, vertex):  # The distance between the center and a vertex
        return self.center.free_edges[vertex.id].length

    def weight(self):
        return sum([sum([vertex1.edges[vertex2.id].length for vertex2 in self.vertices]) for vertex1 in self.vertices])


def mykmeans(k, array):  # Main function
    workgraph = AgregGraph(array)  # Creating an Graph object corresponding to the given graph
    seeds = eval(f'bs.{config["BASESEEDS"]}')(workgraph, k)
    allseeds = list()
    pools = list()
    count = 0
    while set(seeds) not in allseeds:  # While the seeds change on each iteration, creating new clusters from them
        logging.debug(str(allseeds))  # debug
        allseeds.append(set(seeds))
        # New graph to work on
        workgraph = AgregGraph(array)
        workgraph.agreg(seeds)
        seeds = [pool.center.id for pool in
                 workgraph.pools]  # Re-defining seeds as the centers of just created clusters
        pools.append(([[vertex.id for vertex in pool.vertices] for pool in workgraph.pools], workgraph.calc_dist()))
        count += 1
        logging.info(f'Loops: {count}')
    print(f'Total loops: {count}')
    return min(pools, key=lambda t: t[1])


logging.basicConfig(filename=dirname + '/resources/kmeans.log', level=logging.DEBUG)
logging.info(f"-------------New execution {time.asctime()}-------------")
# graph = numpy.array(genweightgraph(n,-100,100))#debug
