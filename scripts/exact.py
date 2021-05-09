import os
import numpy as np


def total(pool, dist_mat):
    return sum([dist_mat[i][j] for c, i in enumerate(pool) for j in pool[c + 1:]])


def best_sol(n, k, dist_mat):
    table = np.zeros((n // k, k), dtype=int)
    return constr_sol_rec(0, 1, n // k, k, table, list(range(1, n)), 0, dist_mat)


def constr_sol_rec(col, lig, p, k, table, rest, tot, dist_mat):
    table2 = np.copy(table)
    if lig == 0 and col == len(table[0]) - 1:
        table2[:, col] = rest
        return table2, tot + total(table2[:, col], dist_mat)
    elif lig == 0:
        beg, end = table[0, col - 1] + 1, col * p + 1
        tot += total(table[:, col - 1], dist_mat)
    else:
        beg, end = table[lig - 1, col] + 1, k * (p - 1) + lig + 2
    res = list()
    for i in range(beg, end):
        if i in rest:
            rest2 = rest.copy()
            rest2.remove(i)
            table2[lig, col] = i
            rec = recfunc(col + (lig + 1) // p, (lig + 1) % p, p, k, table2, rest2, tot, dist_mat)
            res.append(rec)
    try:
        return min(res, key=lambda r: r[1])
    finally:
        return table, np.inf
        # print(f'lig={lig},col={col},beg={beg},end={end},rest={rest},table={table}')
        # assert False

