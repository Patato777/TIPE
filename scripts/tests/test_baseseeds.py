import os
import logging
import tkinter

import numpy as np

from scripts import baseseeds as bs
from scripts import display_results as dp
from scripts import kmeans_new as kmeans

dirname = os.path.dirname(__file__)


def test():
    with open(dirname + '/resources/Table_distances_Essonne_py.txt', 'r') as f:
        dist_table = np.array(eval(f.read()))

    with open(dirname + '/resources/Liste_pos_Essonne_py.txt', 'r') as f:
        cities = eval(f.read())

    with open(dirname + '/resources/liste_essonne_py.txt') as f:
        names = eval(f.read())

    graph = kmeans.AgregGraph(dist_table)
    seeds = bs.kmpp(graph, 7)
    for k in range(1, 8):
        dp_main = dp.Main(cities, names)
        plots = [dp_main.map.plot(vertex[0], vertex[1], dp.label(vertex[2])) for vertex in dp_main.pop.pop]
        for seed in seeds[:k]:
            dp_main.map.colorise(plots[seed], "#ff0000")
            logging.info(dp_main.pop.pop[seed])
        next_btn = tkinter.Button(dp_main.root, text="Next", command=lambda: dp_main.root.destroy())
        next_btn.pack()
        try:
            dp_main.root.mainloop()
        finally:
            pass
