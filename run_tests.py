import logging
import time

logging.basicConfig(filename='scripts/tests/resources/test.log', level=logging.INFO)
logging.info(f'--------- {time.asctime()} ----------')

import scripts.tests.test_genetic
