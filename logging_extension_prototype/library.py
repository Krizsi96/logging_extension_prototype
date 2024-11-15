import logging
import time

logger = logging.getLogger(__name__)

def time_keeper():
    current_time = time.time()
    logger.info(f"{current_time}")

if __name__ == '__main__':
    logger.addHandler(logging.StreamHandler())
    logger.setLevel(logging.DEBUG)

    for i in range(10):
        time_keeper()