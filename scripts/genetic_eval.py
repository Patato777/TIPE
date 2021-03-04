import configparser
import logging
import os
import sqlite3
import time

import scripts.genetic as gen

dirname = os.path.dirname(__file__)

logging.basicConfig(filename='resources/gen.log', level=logging.INFO)
logging.info(f'--------- Genetic eval: {time.asctime()} ----------')

conf = configparser.ConfigParser()
conf.read(dirname + '/resources/config')
config = conf['gen_eval']

with open(dirname + config["DATASET_PATH"], 'r') as datafile:
    dist_table = eval(datafile.read())

conn = sqlite3.connect(dirname + '/resources/genetic.db')
curs = conn.cursor()

params = eval(config["GEN_PARAMS"])
curs.execute(f"CREATE TABLE {config['DATASET_NAME']} {(*params.keys(), 'scores', 'generation')}")
logging.info(params)


def rec(values, param):
    if not param:
        if not (values[3] == '-1' and values[5] == 'linear'):
            logging.info(values)
            gen_main = gen.Main(dist_table, int(config["DATALEN"]), int(config["POOLS_COUNT"]))
            chroms_fits = gen_main.mainloop(int(config["LOOPS_COUNT"]), True)
            logging.debug(f"INSERT INTO {config['DATASET_NAME']} VALUES ({'?,' * (len(values) + 1)}?)")
            for fits, generation in chroms_fits:
                logging.debug((*values, str(fits), str(generation)))
                curs.execute(f"INSERT INTO {config['DATASET_NAME']} VALUES ({'?,' * (len(values) + 1)}?)",
                             (*values, str(fits), str(generation)))
            conn.commit()
    else:
        for value in params[param[0]]:
            logging.debug((values, param))
            logging.debug((params[param[0]], value))
            conf['genetic'][param[0]] = str(value)
            with open(dirname + '/resources/config', 'w') as conffile:
                conf.write(conffile)
            rec(values + (str(value),), param[1:])


rec((), list(params.keys()))
