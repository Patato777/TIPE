import scripts.genetic as gen
import scripts.operators as op
import logging

c1 = gen.Chromosome([1, 2, 3, 4, 5, 6, 7, 8], 8)
c2 = gen.Chromosome([2, 4, 6, 8, 1, 3, 5, 7], 8)

cross = op.Cross('pmx')
logging.info(cross.cross(c1, c2))
