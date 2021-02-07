import os
import random
import numpy as np
import scripts.operators as op

dirname = os.path.dirname(__file__)


class Params:
    def __init__(self):
        with open(dirname + '/resources/config') as f:
            text = f.read()
            beginning = text.find('\n', text.find('<genetic>'))
            end = text.find('</genetic>')
            config = text[beginning:end]
        for line in config.splitlines():
            exec('self.' + line)


class Distances:
    def __init__(self, mat):
        self.matrix = np.array(mat)

    def in_pool(self, pool):
        return sum([self.matrix[i, j] for c, i in enumerate(pool) for j in pool[i + 1:]])

    def total(self, pools):
        return sum([self.in_pool(pool) for pool in pools])


class Chromosome:
    def __init__(self, chrom):
        self.id = chrom


class Main:
    def __init__(self, dist, n, k):
        self.params = Params()
        self.distances = Distances(dist)
        self.n, self.k = n, k
        self.pop = Population()
        self.pop.gen_random(n, self.params.POPSIZE)

    def fitness(self, chromosome):
        return self.distances.total(
            [chromosome[i * (self.n // self.k):(i + 1) * (self.n // self.k)] for i in range(self.k)])

    def generation(self):
        new_pop = Population()
        selection = op.Selection(self.fitness, self.pop, self.params.SELECTION)
        for _ in range(self.params.POPSIZE // 2):
            p1, p2 = selection.select()
            new_pop.id.extend(op.Cross(self.params.CROSS).cross(p1, p2))#TODO: define cross methods
        for chrom in new_pop.id:
            op.Mutation(self.params.MUTATION, self.params.MUT_PROB).mutate(chrom)#TODO: define mutation
        self.pop = new_pop


class Population:
    def __init__(self, pop=None):
        if pop is None:
            pop = list()
        self.id = pop

    def gen_random(self, n, size):
        self.id = [Chromosome(random.sample(list(range(n)), n)) for _ in range(size)]
