import logging

class Tournament:
    def __init__(self, dist_table, pool_count):
        self.nodes = [Node(row, dist) for row, dist in enumerate(dist_table)]
        self.n_count = len(self.nodes)
        self.p_count = pool_count
        self.n_per_p = self.n_count // self.p_count
        self.pools = [Pool([])] * self.p_count
        self.update_pools()

    def update_pools(self):
        for p in range(self.p_count):
            nodes = self.nodes[p * self.n_per_p:(p + 1) * self.n_per_p]
            if nodes != self.pools[p].nodes:
                self.pools[p] = Pool(nodes)

    def calc_weight(self):
        return sum([pool.calc_weight() for pool in self.pools])

    def swap(self, node1, node2):
        self.nodes[node1.pos], self.nodes[node2.pos] = self.nodes[node2.pos], self.nodes[node1.pos]
        node1.pos, node2.pos = node2.pos, node1.pos
        self.update_pools()


class Node:
    def __init__(self, id, dist):
        self.id = id
        self.pos = id
        self.dist = dist

    def dist_to_p(self, pool):
        return sum([self.dist[n.id] for n in pool.nodes])


class Pool:
    def __init__(self, nodes):
        self.nodes = nodes
        for node in self.nodes:
            node.weight = node.dist_to_p(self)

    def calc_weight(self):
        weight = 0
        for node in self.nodes:
            weight += sum([node.dist[node2.id] for node2 in self.nodes])
        return weight


class Two_opt:
    def __init__(self, dataset, pool_count):
        self.tournament = Tournament(dataset, pool_count)

    def two_opt(self):
        logging.info(f'Total weight: {self.tournament.calc_weight()}')
        better = True
        loop = 0
        while better:
            loop += 1
            if not loop % 200:
                logging.info(f'Loop: {loop}')
                logging.debug(f'{[node.id for node in self.tournament.nodes]}')
            better = False
            for p, pool1 in enumerate(self.tournament.pools):
                for pool2 in self.tournament.pools[p + 1:]:
                    for node1 in pool1.nodes:
                        new_dist1 = node1.dist_to_p(pool2)
                        for node2 in pool2.nodes:
                            new_dist = new_dist1 + node2.dist_to_p(pool1)
                            old_dist = node1.weight + node2.weight
                            if new_dist < old_dist:
                                if not loop % 25000:
                                    logging.debug(f'Node1: {node1.id}, Node2: {node2.id}')
                                self.tournament.swap(node1, node2)
                                better = True
                                break
                        if better:
                            break
                    if better:
                        break
                if better:
                    break
        logging.info(f'Total loop count: {loop}')
        logging.info(f'Total weight: {self.tournament.calc_weight()}')
        return [[node.id for node in pool.nodes] for pool in self.tournament.pools]
