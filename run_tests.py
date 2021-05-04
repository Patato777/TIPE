import logging
import time

import scripts.tests.test_genetic as test

logging.basicConfig(filename='scripts/tests/resources/test.log', level=logging.INFO)
logging.info(f'--------- {time.asctime()} ----------')

test.test()
