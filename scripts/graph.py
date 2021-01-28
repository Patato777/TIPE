import random,numpy,copy,math

def genweightgraph(n,mini,maxi) :
    graph = [[random.randint(mini,maxi) for k in range(n-1)] for k in range(n)]
    edges = [[math.sqrt(sum([(x[k]-y[k])**2 for k in range(n-1)])) for y in graph] for x in graph]
    return numpy.array(edges)

class Graph :
    def __init__(self,array) :
        self.vertices = [Vertex(k) for k in range(len(array))]
        self.edges = list()
        for k in range(len(array)) :
            for j in range(k,len(array)) :
                self.edges.append(Edge(array[k,j],[self.vertices[k],self.vertices[j]]))
                self.vertices[k].edges[j],self.vertices[j].edges[k] = self.edges[-1],self.edges[-1]
        for vertice in self.vertices :
            vertice.free_edges = vertice.edges.copy()
            del vertice.free_edges[vertice.id]

class Vertex :
    def __init__(self,nb) :
        self.id = nb
        self.edges = dict()
        self.linked_edges = dict()

class Edge :
    def __init__(self,length,between) :
        self.length = length
        self.between = between
