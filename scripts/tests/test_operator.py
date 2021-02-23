import scripts.genetic as gen
import scripts.operators as op
import logging

c1 = gen.Chromosome([0, 1, 2, 3, 4, 5], 6, 2)
c2 = gen.Chromosome([1, 3, 2, 0, 4, 5], 6, 2)

logging.info('---------- Operators ----------')
cross = op.Cross('ap')
logging.info(cross.cross(c1, c2))
