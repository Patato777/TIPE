import configparser
import os
import random
import numpy as np
import scripts.operators as op

dirname = os.path.dirname(__file__)


class Params:
    def __init__(self):
        conf = configparser.ConfigParser()
        conf.read(dirname + '/resources/config')
        self.config = conf['genetic']


class Distances:
    def __init__(self, mat):
        self.matrix = np.array(mat)

    def in_pool(self, pool):
        return sum([self.matrix[i, j] for c, i in enumerate(pool) for j in pool[i + 1:]])

    def total(self, pools):
        return sum([self.in_pool(pool) for pool in pools])


class Chromosome:
    def __init__(self, chrom, n):
        self.id = chrom
        self.size = n


class Main:
    def __init__(self, dist, n, k):
        self.params = Params()
        self.distances = Distances(dist)
        self.n, self.k = n, k
        self.pop = Population()
        self.pop.gen_random(n, int(self.params.config["POPSIZE"]))

    def fitness(self, chromosome):
        return self.distances.total(
            [chromosome[i * (self.n // self.k):(i + 1) * (self.n // self.k)] for i in range(self.k)])

    def generation(self):
        new_pop = Population()
        selection = op.Selection(self.fitness, self.pop, self.params.config["SELECTION"])
        for _ in range(int(self.params.config["POPSIZE"]) // 2):
            p1, p2 = selection.select()
            new_pop.id.extend(op.Cross(self.params.config["CROSS"]).cross(p1, p2))
        for chrom in new_pop.id:
            op.Mutation(self.params.config["MUTATION"], self.params.config["MUT_PROB"]).mutate(chrom)
        self.pop = new_pop


class Population:
    def __init__(self, pop=None):
        if pop is None:
            pop = list()
        self.id = pop

    def gen_random(self, n, size):
        self.id = [Chromosome(random.sample(list(range(n)), n), n) for _ in range(size)]
