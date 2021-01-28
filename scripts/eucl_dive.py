from graph import *

class GraphtoEucl(Graph) :
    def plongeuclide(self) :
        for k,vertex in enumerate(self.vertices) :
            vertex.coords = [0]*(len(self.vertices)-1)
            d02 = vertex.edges[0].length**2
            for i in range(1,k) :
                di2 = vertex.edges[i].length**2
                somme2coordsi = sum([c**2 for c in self.vertices[i].coords])
                prodcrois = sum([vertex.coords[j]*self.vertices[i].coords[j] for j in range(len(vertex.coords))])
                vertex.coords[i-1] = ((d02-di2+somme2coordsi-2*prodcrois)/(2*self.vertices[i].coords[i-1]))
                #print(str(i)+'bite')
            if k > 0 :
                vertex.coords[k-1] = math.sqrt(vertex.edges[0].length**2-sum([c**2 for c in vertex.coords]))
            #print(k)

