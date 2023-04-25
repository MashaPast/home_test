import logging
import time

timestamp = int(time.time())
logging.basicConfig(filemode='w', format='%(asctime)s %(levelname)s %(message)s', level=logging.INFO)

log = logging
