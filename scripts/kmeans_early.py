import random
import numpy

class Graph :
    def __init__(self,array) :
        self.nodes = [Node(k) for k in range(len(array))]
        self.vertices = list()
        for k in range(len(array)) :
            for j in range(k+1,len(array)) :
                self.vertices.append(Vertice(array[k,j],[self.nodes[k],self.nodes[j]]))
                self.nodes[k].vertices[j],self.nodes[j].vertices[k] = self.vertices[-1],self.vertices[-1]
        for node in self.nodes :
            node.free_vertices = node.vertices
        
class Node :
    def __init__(self,nb) :
        self.id = nb
        self.vertices = dict()
        self.linked_vertices = dict()

class Vertice :
    def __init__(self,length,between) :
        self.length = length
        self.between = between

class Pool :
    def __init__(self,nb) :
        self.id = nb
        self.size = 0
        self.nodes = list()

        
def agreg(graph,k) :
    pools = [Pool(i) for i in range(k)]
    seeds = list()
    seeds.extend(max(graph.vertices,key=lambda v : v.length).between)
    for seed in range(k-2) :
        seeds.append(max(graph.nodes,key=lambda n : sum([n.vertices[s.id] for s in seeds])))
    for i in range(k) :
        pools[i].nodes.append(seeds[i])
        pools[i].center = seeds[i]s
        for j in range(k) :
            if j != i :
                del seeds[i].free_vertices[seeds[j].id]
    for augment in range(k) :
        new_nodes = dict()
        for pool in pools :
            pool.new_node = graph.node[min(pool.center.vertices,key=lambda i : pool.center.vertices[i].length)]
            new_nodes[pool.id] = pool.new_node
    
