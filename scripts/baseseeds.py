import random
from numpy import array,delete,copy

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
    all_dist = copy(dist_mat)
    clusters = {k:[k] for k in range(len(dist_mat))}
    for i in range(len(dist_mat)-k) :
        n = len(dist_mat)
        group = min([(x,y) for x in range(n) for y in range(n) if x!=y], key=lambda i:dist_mat[i[0],i[1]])
        if group[0] == 0 :
            near = 1
        else :
            near = -1
        dist_mat[:,[group[0]+near,group[1]]] = dist_mat[:,[group[1],group[0]+near]]
        dist_mat[[group[0]+near,group[1]]]=dist_mat[[group[1],group[0]+near]]
        clusters[group[0]+near],clusters[group[1]] = clusters[group[1]],clusters[group[0]+near]
        new_dist = [(dist_mat[group[0],k]+dist_mat[group[0]+near,k])/2 for k in range(len(dist_mat))]
        dist_mat[group[0]],dist_mat[:,group[0]] = new_dist,new_dist
        dist_mat=delete(delete(dist_mat,group[0]+near,0),group[0]+near,1)
        clusters[group[0]].extend(clusters[group[0]+near])
        for j in range(group[0]+near,n-1) :
            clusters[j],clusters[j+1] = clusters[j+1],clusters[j]
        clusters.pop(n-1)
    return [min([k for k in values],key=lambda k:sum([all_dist[k,n] for n in values])) for values in clusters.values()]
