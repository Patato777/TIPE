import os,numpy
from scripts.display_results import *
from scripts.kmeans_new import *
from scripts.post_permut import *

dirname = os.path.dirname(__file__)

with open(dirname+'/resources/Table_distances_Essonne_py.txt','r') as f :
    dist_table = eval(f.read())

with open(dirname+'/resources/Liste_pos_Essonne_py.txt','r') as f :
    cities = eval(f.read())

with open(dirname+'/resources/liste_essonne_py.txt') as f :
    names = eval(f.read())

#pop = random.choices(cities,k=30)
#dist = [dist_table[cities.index(c)] for c in pop]
pop = cities
dist = dist_table

array = numpy.array(dist)
#print(array)
poolsl = list()
param = 1
for k in range(param) :
    try :
        poolsl.append(mykmeans(7,array))
    except Exception as error:
        print(error)
        continue
    print(f'In progress: {100*k/param}%')
print('Completed!')
bestpools = min(poolsl,key=lambda t:t[1])
betpools = bettergraph(bestpools[0],dist_table)
print(betpools)
pools = betpools[0]
#print(pools)

main = Main(pop,names)
main.dispool(pools)

main.root.mainloop()

