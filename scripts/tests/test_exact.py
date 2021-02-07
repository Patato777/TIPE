from scripts.exact import *

dirname = os.path.dirname(__file__)

with open(dirname+'/resources/Table_distances_Essonne_py.txt','r') as f :
    dist_mat = eval(f.read())

sol = best_sol(12,4,dist_mat)
print(sol)