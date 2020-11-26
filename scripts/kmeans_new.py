import logging,os,random,time
from scripts.graph import *

dirname = os.path.dirname(__file__)
with open(dirname+'/resources/config') as f :
    text = f.read()
    beginning = text.find('\n',text.find('<kmeans>'))
    end = text.find('</kmeans>')
    config = text[beginning:end]
    exec(config)

class AgregGraph(Graph) : #Children class of Graph, for this specific algorithm
    def custom_bs(self,k) :#Choosing the seeds for kmeans
        seeds = list()
        seeds.extend(max(self.vertices,key=lambda v : v.length).between)#Beginning with the 2 most distant nodes 
        for seed in range(k-2) :#Adding the node the furthest away from the barycentre
        #TODO: a seed can be chosen multiple times
            seeds.append(max(self.nodes,key=lambda n : sum([n.vertices[s.id].length for s in seeds])))
        for s in seeds :
            assert seeds.count(s) == 1
        return [seed.id for seed in seeds]#Return a list of ids
    
    def random_bs(self,k) :
        seeds = random.choices(self.nodes,k=k)
        return [seed.id for seed in seeds]

    def agreg(self,seeds) :#Agregation of nodes around the seeds
        k = len(seeds)#Number of clusters
        #Associating ids to the corresponding nodes
        seeds = [self.nodes[seed] for seed in seeds]
        #Creating k clusters, each containing a different seed
        self.pools = [Pool(i) for i in range(k)]
        for i in range(k) :
            self.pools[i].nodes.append(seeds[i])
            self.pools[i].center = seeds[i]
            for node in self.nodes :
                if node.id != seeds[i].id :
                    del node.free_vertices[seeds[i].id]#TODO: Wa da fuk?
        #Adding one node to each cluster each time
        for augment in range(len(self.nodes)//k-1) :
            new_nodes = list()
            for pool in self.pools :
                logging.debug(str(pool.center.free_vertices))#debug
                #Adding the nearest node from the center of the pool
                free_nodes = [self.nodes[i] for i in pool.center.free_vertices]
                pool.new_node = min(free_nodes,key=eval(f'pool.{DISTTONODE}'))
                logging.debug(str([nod.id for nod in pool.nodes]))#debug
                #Eliminating the connection to the other nodes
                for node in self.nodes :
                    try :
                        if node.id != pool.new_node.id :
                            del node.free_vertices[pool.new_node.id]
                    except Exception as error :#TODO: Why does it throw that f***g error
                        logging.debug(f'error:{error}, node:{node.id}, new node:{pool.new_node.id}, node.free vertices:{node.free_vertices.keys()}, new_node.free vertices:{pool.new_node.free_vertices.keys()}')
                while pool.new_node in new_nodes :#It probably shouldn't happen... (I think?)
                    #Anyway, if 2 clusters try to aggregate the same node
                    self.conflict(pool,pool.new_node.pool)
                    logging.debug("C'est une boucle infinie MDR")#debug
                new_nodes.append(pool.new_node)
                pool.new_node.pool = pool
                pool.nodes.append(pool.new_node)
                pool.center = min(pool.nodes,key = lambda n : pool.dist_to_node(n))#Re-defining the center of the pool
    
    def conflict (self, pool1,pool2) :#If 2 clusters try to aggregate the same node
        node = pool1.new_node
        pool = max((pool1,pool2),key=lambda p : p.dist_to_node(node))
        pool.new_node = min(self.nodes,key=eval(f'pool.{DISTTONODE}'))

    def calc_dist (self) :
        return sum([pool.weight() for pool in self.pools])
    
class Pool :#Class of clusters
    def __init__(self,nb) :
        self.id = nb
        self.size = 0
        self.nodes = list()

    def dist_to_node(self,node) :#The distance to a node #TODO: use this instead of centers during aggregation
        return sum([node.vertices[pnode.id].length for pnode in self.nodes])

    def to_center(self,node) : #The distance between the center and a node
        return self.center.free_vertices[node.id].length

    def weight(self) :
        return sum([sum([node1.vertices[node2.id].length for node2 in self.nodes]) for node1 in self.nodes])

def mykmeans(k,array) :#Main function
    workgraph = AgregGraph(array)#Creating an Graph object corresponding to the given graph
    seeds = eval(f'workgraph.{BASESEEDS}')(k)
    allseeds = list()
    pools = list()
    count = 0
    while set(seeds) not in allseeds :#While the seeds change on each iteration, creating new clusters from them
        logging.debug(str(allseeds))#debug
        allseeds.append(set(seeds))
        #New graph to work on
        workgraph = AgregGraph(array)
        workgraph.agreg(seeds)
        seeds = [pool.center.id for pool in workgraph.pools]#Re-defining seeds as the centers of just created clusters
        pools.append(([[node.id for node in pool.nodes] for pool in workgraph.pools],workgraph.calc_dist()))
        count += 1
        logging.info(f'Loops: {count}')
    return min(pools,key=lambda t : t[1])

logging.basicConfig(filename=dirname+'/resources/kmeans.log', level=logging.DEBUG)
logging.info(f"-------------New execution {time.asctime()}-------------")
#graph = numpy.array(genweightgraph(n,-100,100))#debug
