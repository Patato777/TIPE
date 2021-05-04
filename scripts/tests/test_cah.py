import os

from numpy import array, delete, copy


def test():
    f = open(os.path.dirname(__file__) + '/resources/Table_distances_Essonne_py.txt', 'r')
    dist_mat = array(eval(f.read()))
    f.close()

    initdist_mat = copy(dist_mat)
    k = 7
    clusters = {k: [k] for k in range(len(dist_mat))}
    for i in range(len(dist_mat) - k):
        n = len(dist_mat)
        group = min([(x, y) for x in range(n) for y in range(n) if x != y], key=lambda i: dist_mat[i[0], i[1]])
        if group[0] == 0:
            near = 1
        else:
            near = -1
        dist_mat[:, [group[0] + near, group[1]]] = dist_mat[:, [group[1], group[0] + near]]
        dist_mat[[group[0] + near, group[1]]] = dist_mat[[group[1], group[0] + near]]
        clusters[group[0] + near], clusters[group[1]] = clusters[group[1]], clusters[group[0] + near]
        new_dist = [(dist_mat[group[0], k] + dist_mat[group[0] + near, k]) / 2 for k in range(len(dist_mat))]
        dist_mat[group[0]], dist_mat[:, group[0]] = new_dist, new_dist
        dist_mat = delete(delete(dist_mat, group[0] + near, 0), group[0] + near, 1)
        clusters[group[0]].extend(clusters[group[0] + near])
        for j in range(group[0] + near, n - 1):
            clusters[j], clusters[j + 1] = clusters[j + 1], clusters[j]
        clusters.pop(n - 1)
    print(
        [min([k for k in values], key=lambda k: sum([initdist_mat[k, n] for n in values])) for values in
         clusters.values()])
