import logging
import random


class Operator:
    pass


class Selection(Operator):
    def __init__(self, fit, pop, select, scale='inverse_scal', window=0):
        self.fitness = fit
        self.pop = pop
        self.window = window
        if select == 'wheel':
            self.evaluate()
            self.select = self.wheel
        self.scale = eval(f'self.{scale}()')

    def evaluate(self):
        for chrom in self.pop.id:
            chrom.fit = self.fitness(chrom.id) - self.window

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
        std_dev = (sum([c.fit ** 2 for c in self.pop]) / len(fits) - mean) ** (1 / 2)
        sigma = std_dev if std_dev else 1
        return [1 + (mean - c.fit) / (2 * sigma) for c in self.pop.id]


class Cross(Operator):
    def __init__(self, cross):
        cross_dic = dict(pmx=self.pmx,cx=self.cx)
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
        chrs = [(chr1.id,rest1),(chr2.id,rest2)]
        for pos in range(chr1.size):
            random.shuffle(chrs)
            logging.debug(f'pos: {pos}')
            if off1[pos] == None:
                logging.debug('Is None')
                g1, g2 = chrs[0][0][pos], chrs[1][0][pos]
                off1[pos] = g1
                off2[pos] = g2
                try :
                    chrs[0][1].remove(g1)
                    chrs[1][1].remove(g2)
                except Exception as error :
                    logging.error(f'g1: {g1}, g2: {g2}, chrs: {chrs}, off1: {off1}, off2: {off2}')
                    raise error
                while g1 in chrs[0][1] or g1 in chrs[1][1]:
                    logging.debug(f'g1: {g1},g2: {g2},chrs[0][1]: {chrs[0][1]},chrs[1][1]: {chrs[1][1]}')
                    if g1 in chrs[0][1]:
                        pos1 = chrs[0][0].index(g1)
                        g2 = g1
                        g1 = chrs[1][0][pos1]
                        logging.debug(f'g1: {g1}, g2: {g2}, pos1: {pos1}')
                        try :
                            chrs[1][1].remove(g1)
                            chrs[0][1].remove(g2)
                        except Exception as error:
                            logging.debug(f'off1: {off1}, off2: {off2}')
                            logging.debug('g1 in chrs[0][1]')
                            logging.error(f'chrs[1][1]: {chrs[1][1]},g2: {g2}')
                            logging.error(f'chrs[0][1]: {chrs[1][1]},g1: {g1}')
                            raise error
                    else:
                        pos1 = chrs[1][0].index(g1)
                        g2 = g1
                        g1 = chrs[0][0][pos1]
                        logging.debug(f'g1: {g1}, g2: {g2}, pos1: {pos1}')
                        try :
                            chrs[1][1].remove(g2)
                            chrs[0][1].remove(g1)
                        except Exception as error:
                            logging.debug(f'off1: {off1}, off2: {off2}')
                            logging.debug('g1 in chrs[1][1]')
                            logging.error(f'chrs[1][1]: {chrs[1][1]},g2: {g2}')
                            logging.error(f'chrs[0][1]: {chrs[1][1]},g1: {g1}')
                            raise error
                    off1[pos1] = g1
                    off2[pos1] = g2
        return off1, off2


class Mutation(Operator):
    def __init__(self, mut, prob):
        mut_dic = dict(swap=self.swap, insertion=self.insertion)
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


class Inversion(Operator):
    def __init__(self, inv):
        pass
