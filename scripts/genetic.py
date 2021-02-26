import configparser
import logging
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
    def __init__(self, chrom, n, psize):
        self.id = chrom
        self.size = n
        self.psize = psize


class Main:
    def __init__(self, dist, n, k):
        self.params = Params()
        self.distances = Distances(dist)
        self.n, self.k = n, k
        self.poolsize = n // k
        self.pop = Population()
        self.pop.gen_random(n, n // k, int(self.params.config["POPSIZE"]))
        self.elite = int(int(self.params.config["POPSIZE"]) * float(self.params.config["ELITISM"]))
        self.window = 0
        if int(self.params.config["WINDOWING"]) >= 0:
            self.worst_l = [0] * (int(self.params.config["WINDOWING"]) + 1)

    def fitness(self, chromosome):
        return self.distances.total(
            [chromosome[i * (self.n // self.k):(i + 1) * (self.n // self.k)] for i in range(self.k)])

    def generation(self):
        new_pop = Population()
        selection = op.Selection(self.pop, self.params.config["SELECTION"], self.params.config["SCALE"],
                                 self.window)
        cross = op.Cross(self.params.config["CROSS"])
        new_pop.id.extend(sorted(self.pop.id, key=lambda c: c.fitness)[:self.elite])
        logging.debug([c.fitness for c in new_pop.id])
        for _ in range((int(self.params.config["POPSIZE"]) - self.elite) // 2):
            p1, p2 = selection.select()
            off1, off2 = cross.cross(p1, p2)
            new_pop.id.extend([Chromosome(off1, self.n, self.poolsize), Chromosome(off2, self.n, self.poolsize)])
        for chrom in new_pop.id[self.elite:]:
            op.Mutation(self.params.config["MUTATION"], float(self.params.config["MUT_PROB"])).mutate(chrom)
        self.pop = new_pop

    def mainloop(self, loops):
        for loop in range(loops):
            for c in self.pop.id:
                c.fitness = self.fitness(c.id)
            if int(self.params.config["WINDOWING"]) >= 0:
                worst = max([c.fitness for c in self.pop.id])
                self.worst_l = self.worst_l[1:] + [worst]
                self.window = max(self.worst_l)
            self.generation()
            logging.info(str(loop))
            logging.info(min([c.fitness for c in self.pop.id]))
        return min([c for c in self.pop.id], key=lambda c: c.fitness).id


class Population:
    def __init__(self, pop=None):
        if pop is None:
            pop = list()
        self.id = pop

    def gen_random(self, n, poolsize, size):
        self.id = [Chromosome(random.sample(list(range(n)), n), n, poolsize) for _ in range(size)]
