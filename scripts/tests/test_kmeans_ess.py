import os,numpy
from scripts.display_results import *
from scripts.kmeans_new import *

dirname = os.path.dirname(__file__)

with open(dirname+'/resources/Table_distances_Essonne_py.txt','r') as f :
    dist_table = eval(f.read())

with open(dirname+'/resources/Liste_pos_Essonne_py.txt','r') as f :
    cities = eval(f.read())

#pop = random.choices(cities,k=30)
#dist = [dist_table[cities.index(c)] for c in pop]
pop = cities
dist = dist_table

array = numpy.array(dist)
print(array)
poolsl = list()
param = 20
for k in range(param) :
    try :
        poolsl.append(mykmeans(7,array))
    except :
        continue
    print(f'In progress: {100*k/param}%')
print('Completed!')
pools = min(poolsl,key=lambda t:t[1])[0]
#print(pools)

main = Main(pop)
main.dispool(pools)

main.root.mainloop()

