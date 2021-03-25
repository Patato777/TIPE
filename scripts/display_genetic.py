import pylab as pl
import sqlite3
import os
import configparser
import logging

dirname = os.path.dirname(__file__)

class Config:
    def __init__(self):
        conf = configparser.ConfigParser()
        conf.read(dirname + '/resources/config')
        self.config = conf['disp_gen']

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(dirname + f'/resources/{db}.db')
        self.curs = self.conn.cursor()

class Main:
    def __init__(self):
        self.config = Config().config
        self.db = Database(self.config['DB'])

    def display(self):
        self.p_set = eval(self.config['p_set'])
        logging.debug(self.p_set.items())
        cond = ' AND '.join([key+'="'+str(val)+'"' for key, val in self.p_set.items()])
        logging.debug(cond)
        self.records = self.db.curs.execute(f'SELECT generation,scores FROM {self.config["TABLE"]} WHERE ' + cond)
        for rec in self.records:
            logging.debug(rec)
            pl.plot(int(rec[0]),int(rec[1]))
        pl.show()
