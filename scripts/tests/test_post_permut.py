import os

from scripts.post_permut import *


def test():
    with open(os.path.dirname(__file__) + '/resources/Table_distances_Essonne_py.txt', 'r') as f:
        dist = eval(f.read())
    pools = [[k for k in range(28 * i, 28 * (i + 1))] for i in range(7)]
    print(pools)
    bett = bettergraph(pools, dist)
    print(bett)
