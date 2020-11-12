from scripts.graph import *
from scripts.kmeans_new import *

arr = genweightgraph(30,-100,100)
print(arr)
p = mykmeans(5,arr)
