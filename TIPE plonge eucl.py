from graph import *

class GraphtoEucl(Graph) :
    def plongeuclide(self) :
        for k,node in enumerate(self.nodes) :
            node.coords = [0]*(len(self.nodes)-1)
            d02 = node.vertices[0].length**2
            for i in range(1,k) :
                di2 = node.vertices[i].length**2
                somme2coordsi = sum([c**2 for c in self.nodes[i].coords])
                prodcrois = sum([node.coords[j]*self.nodes[i].coords[j] for j in range(len(node.coords))])
                node.coords[i-1] = ((d02-di2+somme2coordsi-2*prodcrois)/(2*self.nodes[i].coords[i-1]))
                #print(str(i)+'bite')
            if k > 0 :
                node.coords[k-1] = math.sqrt(node.vertices[0].length**2-sum([c**2 for c in node.coords]))
            #print(k)

