import logging
import os

import numpy

import scripts.display_results as disp
import scripts.genetic as gen


def test():
    dirname = os.path.dirname(__file__)
    with open(dirname + '/resources/Table_distances_Essonne_py.txt', 'r') as f:
        dist_table = eval(f.read())

    with open(dirname + '/resources/Liste_pos_Essonne_py.txt', 'r') as f:
        cities = eval(f.read())

    with open(dirname + '/resources/liste_essonne_py.txt') as f:
        names = eval(f.read())

    pop = cities
    dist = dist_table

    ar = numpy.array(dist)

    main = gen.Main(ar, len(pop), 14)

    logging.info('---------- Genetic ----------')
    best = main.mainloop(1000, False)
    pools = [[c for c in best[14 * k:14 * (k + 1)]] for k in range(14)]

    logging.info(f'best: {best}')
    logging.info(pools)

    dmain = disp.Main(pop, names)
    dmain.dispool(pools)

    dmain.root.mainloop()
