import random


class Operator:
    pass


class Selection(Operator):
    def __init__(self, fit, pop, select, scale='linear_scal'):
        self.fitness = fit
        self.pop = pop
        if select == 'wheel':
            self.evaluate()
            self.select = self.wheel
        self.scale = eval(f'self.{scale}()')

    def evaluate(self):
        for chrom in self.pop:
            chrom.fit = self.fitness(chrom.id)

    def wheel(self):
        return random.choices(self.pop, weights=self.scale, k=2)

    def linear_scal(self):
        fits = [c.fit for c in self.pop]
        tot = sum(fits)
        return [1 - (f / tot) for f in fits]


class Cross(Operator):
    def __init__(self, cross):
        cross_dic = dict(pmx=self.pmx)
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


class Mutation(Operator):
    def __init__(self, mut, prob):
        mut_dic = dict(swap=self.swap, insertion=self.insertion)
        self.prob = prob
        self.mutate = mut_dic[mut]
        # depending on mut, define self.mutate(chrom)

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
