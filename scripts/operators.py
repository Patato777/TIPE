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
        sub_beg, sub_end = sorted(random.sample(list(range(chr1.size)), 2))
        # TODO: complete this


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
