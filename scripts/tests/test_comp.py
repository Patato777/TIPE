import numpy as np
import pylab as pl

from scripts import comparison

dirname = os.path.dirname(__file__)

n_k = [(10, 2), (20, 4), (30, 5), (40, 5), (50, 5), (60, 5), (70, 5), (80, 4), (90, 5), (100, 5), (110, 5), (120, 6),
       (130, 5), (140, 5), (150, 6), (160, 5), (170, 5), (180, 6), (196, 7)]


def test():
    with open(dirname + '/resources/Table_distances_Essonne_py.txt', 'r') as f:
        dist_table = np.array(eval(f.read()))

    res = list()
    for n, k in n_k:
        tc = comparison.TimeComp(dist_table[:n], k)
        rc = comparison.ResComp(dist_table[:n], k)
        res.append((tc.compare(), rc.compare()))

    pl.plot([t[0] for t in n_k], [r[0] for r in res])
    pl.show()
