import logging
import os
import sqlite3
import statistics

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
        lower, mean, upper, median = list(), list(), list(), list()
        records = self.db.curs.execute(selection + cond).fetchall()
        logging.debug('Fetched')
        try:
            srecords = sorted(records, key=lambda r: int(r[0]))
            if not records[0][1].startswith('['):
                records = list(srecords)
                records = [(k, [int(rec[1]) for rec in records[1000 * k:1000 * (k + 1)]]) for k in range(len(records) // 1000)]
            else:
                records = [(int(rec[0]), eval(rec[1])) for rec in srecords]
            logging.debug('Sorted')
            for record in records:
                avg, med = statistics.mean(record[1]), statistics.median(record[1])
                mini, maxi = min(record[1]), max(record[1])
                lower.append(mini)
                mean.append(avg)
                median.append(med)
                upper.append(maxi)
            gen_axis = range(len(records))
            pl.plot(gen_axis, lower)
            pl.plot(gen_axis, mean)
            pl.plot(gen_axis, median)
            pl.plot(gen_axis, upper)
            pl.show()
        except Exception as error:
            with open(dirname + '/tests/resources/rec.txt', 'w') as f:
                f.write(str(records))
            logging.error(error)
