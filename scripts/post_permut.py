import logging


def calc_weight(pools, dist):
    return sum([sum([sum([dist[n1][n2] for n2 in pool]) for n1 in pool]) for pool in pools])


def bettergraph(pools, dist):
    best = calc_weight(pools, dist)
    logging.info(best)
    fpools = [pool.copy() for pool in pools]
    for p in range(len(pools)):
        for n in range(len(pools[p])):
            npools, weight = permut(pools[p][n], pools[p], pools, dist)
            if weight < best:
                fpools, best = npools, weight
                pools = fpools
                for tpool in pools:
                    for tvertex in tpool:
                        try:
                            assert tpool.count(tvertex) == 1
                        except Exception as error:
                            logging.error(p, n, tpool, tvertex)
                            logging.error(tpool, tvertex)
                            raise error
    return fpools, best


def permut(vertex, vertpool, pools, dist):
    best = calc_weight(pools, dist)
    fpools = pools.copy()
    opools = [pool for pool in pools if pool != vertpool]
    for opool in opools:
        for overtex in opool:
            vertind, overtind = vertpool.index(vertex), opool.index(overtex)
            opool[overtind], vertpool[vertind] = vertpool[vertind], opool[overtind]
            weight = calc_weight(pools, dist)
            if weight < best:
                fpools = [pool.copy() for pool in pools]
                best = weight
            opool[overtind], vertpool[vertind] = vertpool[vertind], opool[overtind]
    return fpools, best
