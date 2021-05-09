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
        return [genetic.Main(self.data, len(self.data), self.k) for _ in range(self.attempts)]

    def kmeans(self):
        return [kmeans.mykmeans(self.k, self.data) for _ in range(self.attempts)]


class TimeComp(Comparison):
    def compare(self):
        to_t = self.time(self.two_opt) / self.attempts
        gen_t = self.time(self.genetic) / self.attempts
        km_t = self.time(self.kmeans) / self.attempts
        return to_t, gen_t, km_t

    def time(self, method):
        t0 = time.perf_counter()
        method()
        totalt = time.perf_counter() - t0
        return totalt


class ResComp(Comparison):
    def compare(self):
        to_r = min(self.two_opt(), key=lambda p: self.calc_weight(p))
        gen_r = min(self.genetic(), key=lambda p: self.calc_weight(p))
        km_r = min(self.kmeans(), key=lambda p: self.calc_weight(p))
        return to_r, gen_r, km_r
