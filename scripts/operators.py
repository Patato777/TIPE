import logging
import random
from functools import reduce


class Operator:
    pass


class Selection(Operator):
    def __init__(self, pop, select, scale, window):
        self.pop = pop
        self.window = window
        if select == 'wheel':
            self.evaluate()
            self.select = self.wheel
        scale_dic = dict(opp=self.opp_scal, inverse=self.inverse_scal, linear=self.linear_scal, sigma=self.sigma_scal)
        self.scale = scale_dic[scale]()
        logging.debug(self.scale)

    def evaluate(self):
        for chrom in self.pop.id:
            chrom.fit = chrom.fitness - self.window

    def wheel(self):
        return random.choices(self.pop.id, weights=self.scale, k=2)

    def opp_scal(self):
        fits = [c.fit for c in self.pop.id]
        tot = sum(fits)
        return [tot - f for f in fits]

    def inverse_scal(self):
        return [1 / c.fit for c in self.pop.id]

    def linear_scal(self):  # /!\ Needs windowing
        return [-c.fit for c in self.pop.id]

    def sigma_scal(self):
        fits = [c.fit for c in self.pop.id]
        tot = sum(fits)
        mean = tot / len(fits)
        std_dev = (sum([c.fit ** 2 for c in self.pop.id]) / len(fits) - mean) ** (1 / 2)
        sigma = std_dev if std_dev else 1
        return [1 + (mean - c.fit) / (2 * sigma) for c in self.pop.id]


class Cross(Operator):
    def __init__(self, cross):
        cross_dic = dict(pmx=self.pmx, cx=self.cx, er=self.er_2_off, mpx=self.mpx, ap=self.ap, my_vr=self.my_vr)
        self.cross = cross_dic[cross]

    def pmx(self, chr1, chr2):
        beg, end = sorted(random.sample(list(range(chr1.size)), 2))
        sub1 = chr1.id[beg:end]
        sub2 = chr2.id[beg:end]
        logging.debug(str(chr1.id) + str(chr2.id) + str(sub1) + str(sub2))
        off1b = [self.pmx_what_gene(chr1.id[pos], sub1, sub2) for pos in range(beg)]
        off1e = [self.pmx_what_gene(chr1.id[pos], sub1, sub2) for pos in range(end, chr1.size)]
        off2b = [self.pmx_what_gene(chr2.id[pos], sub2, sub1) for pos in range(beg)]
        off2e = [self.pmx_what_gene(chr2.id[pos], sub2, sub1) for pos in range(end, chr1.size)]
        return off1b + sub2 + off1e, off2b + sub1 + off2e

    def pmx_what_gene(self, gene, sub1, sub2):
        while gene in sub2:
            gene = sub1[sub2.index(gene)]
        return gene

    def cx(self, chr1, chr2):
        off1, off2 = [None] * chr1.size, [None] * chr2.size
        rest1, rest2 = chr1.id.copy(), chr2.id.copy()
        chrs = [(chr1.id, rest1), (chr2.id, rest2)]
        for pos in range(chr1.size):
            random.shuffle(chrs)
            logging.debug(f'pos: {pos}')
            if off1[pos] is None:
                logging.debug('Is None')
                g1, g2 = chrs[0][0][pos], chrs[1][0][pos]
                off1[pos] = g1
                off2[pos] = g2
                try:
                    chrs[0][1].remove(g1)
                    chrs[1][1].remove(g2)
                except Exception as error:
                    logging.error(f'g1: {g1}, g2: {g2}, chrs: {chrs}, off1: {off1}, off2: {off2}')
                    raise error
                while g1 in chrs[0][1] or g1 in chrs[1][1]:
                    logging.debug(f'g1: {g1},g2: {g2},chrs[0][1]: {chrs[0][1]},chrs[1][1]: {chrs[1][1]}')
                    if g1 in chrs[0][1]:
                        pos1 = chrs[0][0].index(g1)
                        g2 = g1
                        g1 = chrs[1][0][pos1]
                        logging.debug(f'g1: {g1}, g2: {g2}, pos1: {pos1}')
                        try:
                            chrs[1][1].remove(g1)
                            chrs[0][1].remove(g2)
                        except Exception as error:
                            logging.error(f'chrs[0][1]: {chrs[1][1]},g1: {g1}')
                            raise error
                    else:
                        pos1 = chrs[1][0].index(g1)
                        g2 = g1
                        g1 = chrs[0][0][pos1]
                        logging.debug(f'g1: {g1}, g2: {g2}, pos1: {pos1}')
                        try:
                            chrs[1][1].remove(g2)
                            chrs[0][1].remove(g1)
                        except Exception as error:
                            logging.error(f'chrs[0][1]: {chrs[0][1]},g1: {g1}')
                            raise error
                    off1[pos1] = g1
                    off2[pos1] = g2
        return off1, off2

    def er_2_off(self, chr1, chr2):
        return self.er(chr1, chr2), self.er(chr2, chr1)

    def er(self, c1, c2):
        edge_map = [voisins(c1.id, k).union(voisins(c2.id, k)) for k in range(c1.size)]
        off = list()
        for g in c1.id:
            if g not in off:
                off.append(g)
                while edge_map[g]:
                    adj: int
                    for adj in edge_map[g]:
                        edge_map[adj].remove(g)

                    def edge_genes_score(gene):
                        size = len(edge_map[gene])
                        malus = 0 if c1.id.index(g) // c1.psize == c1.id.index(gene) // c1.psize else 0.5
                        return size + malus

                    g = min(edge_map[g], key=edge_genes_score)
                    off.append(g)
        return off

    def mpx(self, chr1, chr2):
        sub_length = random.randint(10, chr1.size // 2)
        beg = random.randint(0, chr1.size - sub_length)
        sub1, sub2 = chr1.id[beg:beg + sub_length], chr2.id[beg:beg + sub_length]
        sub_compl1, sub_compl2 = chr1.id.copy(), chr2.id.copy()
        for g in range(sub_length):
            sub_compl2.remove(sub1[g])
            sub_compl1.remove(sub2[g])
        off1 = sub1 + sub_compl2
        off2 = sub2 + sub_compl1
        return off1, off2

    def ap(self, chr1, chr2):
        chrs1 = (chr1, chr2)
        chrs2 = (chr2, chr1)
        off1, off2 = list(), list()
        for k in range(2 * chr1.size):
            if chrs1[k % 2].id[k // 2] not in off1:
                off1.append(chrs1[k % 2].id[k // 2])
            if chrs2[k % 2].id[k // 2] not in off2:
                off2.append(chrs2[k % 2].id[k // 2])
        return off1, off2

    def my_vr(self, chr1, chr2):
        pools1 = [set(chr1.id[chr1.psize * p:chr1.psize * (p + 1)]) for p in range(chr1.size // chr1.psize)]
        pools2 = [set(chr2.id[chr2.psize * p:chr2.psize * (p + 1)]) for p in range(chr2.size // chr2.psize)]
        common_sub1 = [reduce(lambda s1, s2: s1.union(s2), [pool1.intersection(pool2) for pool1 in pools1 if
                                                            len(pool1.intersection(pool2)) > 1], set()) for pool2 in
                       pools2]
        common_sub2 = [reduce(lambda s1, s2: s1.union(s2), [pool1.intersection(pool2) for pool2 in pools2 if
                                                            len(pool1.intersection(pool2)) > 1], set()) for pool1 in
                       pools1]
        logging.debug(common_sub1)
        logging.debug(common_sub2)
        unused = reduce(lambda s1, s2: s1.intersection(s2), [set(chr1.id).difference(com) for com in common_sub1])
        for g in unused:
            voisin = [pool for pool in pools1 if g in pool][0].union([pool for pool in pools2 if g in pool][0])
            pool1 = max(range(chr1.size // chr1.psize), key=lambda p: len(voisin.intersection(common_sub1[p])))
            pool2 = max(range(chr1.size // chr1.psize), key=lambda p: len(voisin.intersection(common_sub2[p])))
            common_sub1[pool1].add(g)
            common_sub2[pool2].add(g)
        return reduce(lambda off, pool: off + list(pool), common_sub1, []), reduce(lambda off, pool: off + list(pool),
                                                                                   common_sub2, [])


def voisins(liste, k):
    ind = liste.index(k)
    return {liste[ind - 1], liste[(ind + 1) % len(liste)]}


class Mutation(Operator):
    def __init__(self, mut, prob):
        mut_dic = dict(swap=self.swap, insertion=self.insertion, sim=self.sim)
        self.prob = prob
        self.mutate = mut_dic[mut]

    def swap(self, chrom):
        for gene in range(chrom.size):
            if random.random() < self.prob:
                gene2 = random.choice(list(range(chrom.size)))
                chrom.id[gene], chrom.id[gene2] = chrom.id[gene2], chrom.id[gene]

    def insertion(self, chrom):
        for pos in range(chrom.size):
            if random.random() < self.prob:
                place = random.choice(list(range(chrom.size)))
                gene = chrom.id.pop(pos)
                chrom.id.insert(place, gene)

    def sim(self, c):
        beg, end = sorted(random.sample(list(range(c.size)), 2))
        c.id[beg:end] = reversed(c.id[beg:end])


class Inversion(Operator):
    def __init__(self, inv):
        inv_dic = dict(scramble_pools=self.pscramble, scramble_order=self.oscramble)
        self.inv = inv_dic[inv]

    def pscramble(self, c):
        for p in range(c.n // c.psize):
            pool = c.id[p * c.psize:(p + 1) * c.psize]
            random.shuffle(pool)
            c.id[p * c.psize:(p + 1) * c.psize] = pool

    def oscramble(self, c):
        order = random.sample(range(c.n // c.psize), c.n // c.psize)
        c.id = [c.id[p * c.psize:(p + 1) * c.psize] for p in order]
