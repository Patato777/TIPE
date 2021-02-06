import os
import numpy as np

with open(os.path.abspath('./tests/resources/Table_distances_Essonne_py.txt'), 'r') as f:
    dist_mat = eval(f.read())


def total(pool):
    return sum([dist_mat[i][j] for c, i in enumerate(pool) for j in pool[c + 1:]])


def func(n, k):
    table = np.zeros((n // k, k), dtype=int)
    return recfunc(0, 1, n // k, k, table, list(range(1, n)), 0, 0)


def recfunc(col, lig, p, k, table, rest, tot, prof):
    table2 = np.copy(table)
    if lig == 0 and col == len(table[0]) - 1:
        table2[:, col] = rest
        return table2, tot + total(table[:, col])
    elif lig == 0:
        beg, end = table[0, col - 1] + 1, col * p + 1
        tot += total(table[:, col - 1])
    else:
        beg, end = table[lig - 1, col] + 1, k * (p - 1) + lig
    res = list()
    for i in range(beg, end):
        if i in rest:
            rest2 = rest.copy()
            rest2.remove(i)
            table2[lig, col] = i
            rec = recfunc(col + (lig + 1) // p, (lig + 1) % p, p, k, table2, rest2, tot, prof + 1)
            res.append(rec)
    try:
        return min(res, key=lambda r: r[1])
    except Exception as error:
        return table,tot**2
    # print(f'lig={lig},col={col},beg={beg},end={end},rest={rest},table={table}')


test = func(20, 5)
print(test)
