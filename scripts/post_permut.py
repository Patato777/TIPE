def calc_weight(pools,dist) :
    return sum([sum([sum([dist[n1][n2] for n2 in pool]) for n1 in pool]) for pool in pools])

def bettergraph(pools,dist) :
    best = calc_weight(pools,dist)
    print(best)
    fpools = [pool.copy() for pool in pools]
    for p in range(len(pools)) :
        for n in range(len(pools[p])) :
            npools,weight = permut(pools[p][n],pools[p],pools,dist)
            if weight < best :
                fpools,best = npools,weight
                pools = fpools
                for tpool in pools :
                    for tnode in tpool :
                        try :
                            assert tpool.count(tnode) == 1
                        except Exception as error :
                            print(k,i,pool,node)
                            print(tpool,tnode)
                            raise error
    return fpools, best

def permut(node,nodpool,pools,dist) :
    best = calc_weight(pools,dist)
    fpools = pools.copy()
    opools = [pool for pool in pools if pool!=nodpool]
    for opool in opools : 
        for onode in opool :
            nodind,onodind = nodpool.index(node),opool.index(onode)
            opool[onodind],nodpool[nodind] = nodpool[nodind],opool[onodind] 
            weight = calc_weight(pools,dist)
            if weight < best : 
                fpools = [pool.copy() for pool in pools]
                best = weight
            opool[onodind],nodpool[nodind] = nodpool[nodind],opool[onodind] 
    return fpools, best
