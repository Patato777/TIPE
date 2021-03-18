import pylab as pl
import sqlite3
import os
import configparser
import logging

conf = configparser.ConfigParser()
conf.read(dirname + '/resources/config')
config = conf['disp_gen']

dirname = os.path.dirname(__file__)

conn = sqlite3.connect(dirname + '/resources/genetic.db')
curs = conn.cursor()

p_set = eval(config['p_set'])

cond = ' AND '.join([key+'='+val for key, val in p_set])
logging.debug(cond)

records = curs.execute(f'SELECT {config["generation"]},{config["score"]} FROM {config["TABLE"]} WHERE ' + cond)

for rec in records:
    pl.plot(int(rec[0]),int(rec[1]))

pl.show()
