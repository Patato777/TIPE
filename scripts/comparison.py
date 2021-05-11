import logging
import random
import time

from scripts import genetic
from scripts import kmeans_new as kmeans
from scripts import twoopt


class Comparison:
    def __init__(self, data, k, attempts=1):
        self.data = data
        self.k = k
        self.attempts = attempts

    def calc_weight(self, pools):
        return sum([sum([self.data[node1][node2] for node2 in pool for node1 in pool]) for pool in pools])

    def two_opt(self):
        return [twoopt.Two_opt(self.data, self.k).two_opt() for _ in range(self.attempts)]

    def genetic(self):
        n = len(self.data)
        results = [list(genetic.Main(self.data, n, self.k).mainloop(1300, False))[0] for _ in range(self.attempts)]
        n_k = n // self.k
        return [[[gene for gene in res[j * n_k:(j + 1) * n_k]] for j in range(self.k)] for res in results]

    def kmeans(self):
        return [kmeans.mykmeans(self.k, self.data) for _ in range(self.attempts)]

    def rd(self):
        results = [list(range(len(self.data))) for _ in range(self.attempts)]
        for result in results:
            random.shuffle(result)
        n_k = len(self.data) // self.k
        return [[[gene for gene in res[j * n_k:(j + 1) * n_k]] for j in range(self.k)] for res in results]


class TimeComp(Comparison):
    def compare(self):
        to_t = self.time(self.two_opt) / self.attempts
        logging.debug('2-opt')
        gen_t = self.time(self.genetic) / self.attempts
        logging.debug('genetic')
        km_t = self.time(self.kmeans) / self.attempts
        logging.debug('k-means')
        rd_t = self.time(self.rd) / self.attempts
        logging.debug('random')
        return to_t, gen_t, km_t, rd_t

    def time(self, method):
        t0 = time.perf_counter()
        method()
        totalt = time.perf_counter() - t0
        return totalt


class ResComp(Comparison):
    def compare(self):
        to_r = min([self.calc_weight(p) for p in self.two_opt()])
        logging.debug('2-opt')
        gen_r = min([self.calc_weight(p) for p in self.genetic()])
        logging.debug('genetic')
        km_r = min([self.calc_weight(p[0]) for p in self.kmeans()])
        logging.debug('k-means')
        rd_r = min([self.calc_weight(p) for p in self.rd()])
        logging.debug('random')
        return to_r, gen_r, km_r, rd_r
