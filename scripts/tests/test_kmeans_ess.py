import os,numpy
from scripts.display_results import *
from scripts.kmeans_new import *

dirname = os.path.dirname(__file__)

with open(dirname+'/resources/Table_distances_Essonne_py.txt','r') as f :
    dist_table = eval(f.read())

with open(dirname+'/resources/Liste_pos_Essonne_py.txt','r') as f :
    cities = eval(f.read())

pop = random.choices(cities,k=30)
dist = [dist_table[cities.index(c)] for c in pop]

array = numpy.array(dist)
print(array)
pools = mykmeans(5,array)

main = Main(pop)
main.dispool(pools)

main.root.mainloop()

