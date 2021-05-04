from scripts.twoopt import *
import scripts.display_results as dr
import os

dirname = os.path.dirname(__file__)

def test():
    with open(dirname+'/resources/Table_distances_Essonne_py.txt','r') as f :
        dist_mat = eval(f.read())

    with open(dirname + '/resources/Liste_pos_Essonne_py.txt', 'r') as f:
        pop = eval(f.read())

    with open(dirname + '/resources/liste_essonne_py.txt') as f:
        names = eval(f.read())

    two_opt = Two_opt(dist_mat, 7)
    pools = two_opt.two_opt()

    main_display = dr.Main(pop, names)
    main_display.dispool(pools)

    main_display.root.mainloop()
