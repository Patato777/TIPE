import logging
import os
import sqlite3

import pylab as pl

dirname = os.path.dirname(__file__)


class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(dirname + f'/resources/{db}.db')
        self.curs = self.conn.cursor()


class Main:
    def __init__(self, db):
        self.db = Database(db)

    def display(self, table, p_set):
        self.p_set = p_set
        logging.debug(self.p_set.items())
        cond = ' AND '.join([key + '="' + str(val) + '"' for key, val in self.p_set.items()])
        selection = f'SELECT generation,scores FROM {table} WHERE '
        logging.debug(cond)
        gen = 0
        lower, mid, upper = list(), list(), list()
        while self.db.curs.execute(selection + cond + f' AND generation="{gen}" LIMIT 1').fetchone() is not None:
            records = self.db.curs.execute(selection + cond + f' AND generation="{gen}"')
            avg = 0
            mini, maxi = float('inf'), 0
            for c, rec in enumerate(records):
                avg += int(rec[1])
                mini = min(int(rec[1]), mini)
                maxi = max(int(rec[1]), maxi)
            avg /= c
            lower.append(mini)
            mid.append(avg)
            upper.append(maxi)
            gen += 1
        gen_axis = range(gen - 1)
        pl.plot(gen_axis, lower)
        pl.plot(gen_axis, mid)
        pl.plot(gen_axis, upper)
        pl.show()
