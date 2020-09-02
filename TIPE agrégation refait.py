import tkinter
from graph import *

class AgregGraph(Graph) :
    def baseseeds(self,k) :
        seeds = list()
        seeds.extend(max(self.vertices,key=lambda v : v.length).between)
        for seed in range(k-2) :
            seeds.append(max(self.nodes,key=lambda n : sum([n.vertices[s.id].length for s in seeds])))
        return seeds
            
    def agreg(self,seeds,k) :
        self.pools = [Pool(i) for i in range(k)]
        for i in range(k) :
            self.pools[i].nodes.append(seeds[i])
            self.pools[i].center = seeds[i]
            for node in self.nodes :
                if node.id != seeds[i].id :
                    del node.free_vertices[seeds[i].id]
        for augment in range(k) :
            new_nodes = list()
            for pool in self.pools :
                #print(pool.center.free_vertices)
                pool.new_node = self.nodes[min(pool.center.free_vertices,key=lambda i : pool.center.free_vertices[i].length)]
                #print([nod.id for nod in pool.nodes])
                for node in self.nodes :
                    try :
                        if node.id != pool.new_node.id :
                            del node.free_vertices[pool.new_node.id]
                    except Exception as error :
                        print('error:',error,'node:',node.id,'new node:',pool.new_node.id,'node.free vertices:',node.free_vertices.keys(),'new_node.free vertices:',pool.new_node.free_vertices.keys())
                while pool.new_node in new_nodes :
                    conflict(pool,pool.new_node.pool)
                    print("C'est une boucle infinie MDR")
                new_nodes.append(pool.new_node)
                pool.new_node.pool = pool
                pool.nodes.append(pool.new_node)
                pool.center = min(pool.nodes,key = lambda n : pool.dist_to_node(n))
    
    def conflict (self, pool1,pool2) :
        node = pool1.new_node
        pool = max((pool1,pool2),key=lambda p : p.dist_to_node(node))
        pool.new_node = self.nodes[min(pool.center.free_vertices,key=lambda i : pool.center.free_vertices[i].length)]

class Pool :
    def __init__(self,nb) :
        self.id = nb
        self.size = 0
        self.nodes = list()

    def dist_to_node(self,node) :
        return sum([node.vertices[pnode.id].length for pnode in self.nodes])

def mykmeans(k,graph) :
    workgraph = AgregGraph(graph)
    seeds = workgraph.baseseeds(k)
    allseeds = list()
    while set(seeds) not in allseeds :
        print(allseeds)
        allseeds.append(set(seeds))
        workgraph = AgregGraph(graph)
        workgraph.agreg(seeds,k)
        seeds = [pool.center for pool in workgraph.pools]
    return [[node.id for node in pool.nodes] for pool in workgraph.pools]
    
#graph = numpy.array(genweightgraph(n,-100,100))
