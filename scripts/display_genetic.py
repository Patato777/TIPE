import pylab as pl
import sqlite3
import os
import configparser
import logging

conf = configparser.ConfigParser()
conf.read(dirname + '/resources/config')
config = conf['gen_eval']

dirname = os.path.dirname(__file__)

conn = sqlite3.connect(dirname + '/resources/genetic.db')
curs = conn.cursor()

KEYS = eval(config['KEYS'])
P_SET = eval(config['P_SET'])

cond = ' AND '.join([key+'='+val for key, val in zip(KEYS, P_SET)])
logging.debug(cond)

records = curs.execute(f'SELECT {config["generation"]},{config["score"]} FROM {config["TABLE"]} WHERE ' + cond)

for rec in records:
    pl.plot(int(rec[0]),int(rec[1]))
    logging.debug(rec)

pl.show()
