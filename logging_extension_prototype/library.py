"""
This scripts represents a library that uses logging to show information.
"""
import logging
import time

from logging_extension_prototype.topic_hadler import TopicLogger

logger = logging.getLogger(__name__)
topic_logger = TopicLogger(__name__, logger)

def time_keeper():
    current_time = time.time()
    logger.info(f"{current_time}")

def data_monitor():
    data = {
        'key1': 'value1',
        'key2': 'value2',
        'key3': ['list_item1', 'list_item2'],
    }

    topic_logger.write(data)

if __name__ == '__main__':
    logger.addHandler(logging.StreamHandler())
    logger.setLevel(logging.DEBUG)

    for i in range(10):
        time_keeper()