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
        # depending on cross, define self.cross(p1,p2)
        pass


class Mutation(Operator):
    def __init__(self, mut, prob):
        self.prob = prob
        # depending on mut, define self.mutate(chrom)
