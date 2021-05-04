from scripts.kmeans_new import *


def test():
    arr = genweightgraph(30, -100, 100)
    print(arr)
    p = mykmeans(5, arr)
    return p
