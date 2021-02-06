import os

with open(os.path.abspath('./tests/resources/Table_distances_Essonne_py.txt'), 'r') as f:
    dist_mat = eval(f.read())


def transpositions(n, k):
    return [[i + (n // k) * x, j + (n // k) * y] for i in range(n // k) for j in range(n // k) for x
            in range(k) for y in range(x + 1, k)]


def distance(c, s):
    return sum([dist_mat[i][j] for i in range(c, c + s) for j in range(i + 1, c + s)])


def transposer(repartition, transposition):
    n, k = len(repartition[0]), len(repartition[1])
    repartition2 = [repartition[0].copy(), repartition[1].copy()]
    repartition2[0][transposition[0]], repartition2[0][transposition[1]] = repartition2[0][transposition[1]], \
                                                                           repartition2[0][transposition[0]]
    repartition[1][transposition[0] // k] = distance(transposition[0] // k, n // k)
    repartition[1][transposition[1] // k] = distance(transposition[1] // k, n // k)
    return repartition2


def meilleure_rep(prof, pere, transp):
    if prof < 2:
        fils = list()
        for t in transp:
            if prof == 0:
                print('yo')
            fils.append(transposer(pere, t))
            fils.append(meilleure_rep(prof + 1, fils[-1], transp))
            # print(fils,pere)
        return min([pere] + fils, key=lambda r: sum(r[1]))
    return pere


transp = transpositions(len(dist_mat), 14)
init = [list(range(len(dist_mat))), [distance(i, 14) for i in range(len(dist_mat) // 14)]]
m = meilleure_rep(0, init, transp)
print(m[0] == list(range(len(m[0]))))
