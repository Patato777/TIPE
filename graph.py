import random,numpy,copy,math

def genweightgraph(n,mini,maxi) :
    graph = [[random.randint(mini,maxi) for k in range(n-1)] for k in range(n)]
    vertices = [[math.sqrt(sum([(x[k]-y[k])**2 for k in range(n-1)])) for y in graph] for x in graph]
    return vertices

class Graph :
    def __init__(self,array) :
        self.nodes = [Node(k) for k in range(len(array))]
        self.vertices = list()
        for k in range(len(array)) :
            for j in range(k,len(array)) :
                self.vertices.append(Vertice(array[k,j],[self.nodes[k],self.nodes[j]]))
                self.nodes[k].vertices[j],self.nodes[j].vertices[k] = self.vertices[-1],self.vertices[-1]
        for node in self.nodes :
            node.free_vertices = node.vertices.copy()
            del node.free_vertices[node.id]

class Node :
    def __init__(self,nb) :
        self.id = nb
        self.vertices = dict()
        self.linked_vertices = dict()

class Vertice :
    def __init__(self,length,between) :
        self.length = length
        self.between = between
