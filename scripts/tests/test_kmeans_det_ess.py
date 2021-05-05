import logging
import os
import numpy
import tkinter

import scripts.kmeans_new as kmeans
import scripts.display_results as dp

dirname = os.path.dirname(__file__)


def test():
    with open(dirname + '/resources/Table_distances_Essonne_py.txt', 'r') as f:
        dist_table = numpy.array(eval(f.read()))

    with open(dirname + '/resources/Liste_pos_Essonne_py.txt', 'r') as f:
        cities = eval(f.read())

    with open(dirname + '/resources/liste_essonne_py.txt') as f:
        names = eval(f.read())

    results, seeds = kmeans.mykmeans(7, dist_table, True)
    logging.debug('Completed')
    for pools, seeds_set in zip(results, seeds):
        dp_main = dp.Main(cities, names)
        dp_main.dispool(pools[0], seeds_set)
        next_btn = tkinter.Button(dp_main.root, text="Next", command=lambda: dp_main.root.destroy())
        next_btn.pack()
        try:
            dp_main.root.mainloop()
        finally:
            pass
