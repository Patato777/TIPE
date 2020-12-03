import random
from numpy import array

def verif(seeds) :
    for seed in seeds :
        assert seeds.count(seed) == 1

def custom(self,k) :#Choosing the seeds for kmeans
    seeds = list()
    seeds.extend(max(self.vertices,key=lambda v : v.length).between)#Beginning with the 2 most distant nodes 
    for seed in range(k-2) :#Adding the node the furthest away from the barycentre
    #TODO: a seed can be chosen multiple times
        seeds.append(max(self.nodes,key=lambda n : sum([n.vertices[s.id].length for s in seeds])))
    verif(seeds)
    return [seed.id for seed in seeds]#Return a list of ids

def rd(self,k) :
    seeds = random.choices(self.nodes,k=k)
    return [seed.id for seed in seeds]

def kmpp(self,k) :
    seeds = [random.choice(self.nodes)]
    for s in range(k-1) :
        weights = [min([n.vertices[sd.id].length for sd in seeds]) for n in self.nodes]
        seed = random.choices(self.nodes,weights=weights)[0]
        seeds.append(seed)
    return [seed.id for seed in seeds]

def cah(self,k):
    dist_mat = array([[v.length for v in n.vertices.values()] for n in self.nodes])
    for i in range(len(dist_mat)-k) :
        n = len(dist_mat)
        group = min([[(x,y) for x in range(n) if x!=y] for y in range(n)], key=lambda i:dist_mat[i[0],i[1]])
        if group[0] == 0 :
            pass#Swap columns (a[:, [c0, c1]] = a[:, [c1, c0]]) and rows (a[[c0,c1]]=a[[c1,c0]])
        #TODO: remove a row/column and recalculate distances
       
