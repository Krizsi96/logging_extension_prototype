"""
This scripts represents a cli application that uses the library from the package.
The application has an option to log into a file with json serialization.
"""
import logging
from logging import getLogger
from pathlib import Path
from typing import Annotated

from logging_extension_prototype.library import time_keeper, data_monitor
from logging_extension_prototype.library import logger as library_logger

from logging_extension_prototype.special_handler import SpecialFileHandler

import typer

# Get a logger instance for the application and attach a StreamHandler instance to it
logger = getLogger(__name__)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)

# Attach a StreamHandler instance to the libraries logger
library_logger.addHandler(logging.StreamHandler())
library_logger.setLevel(logging.INFO)

def main():
    logger.info("Hello from logging-extension-prototype!")

    for i in range(10):
        time_keeper()
        data_monitor()

def cli(log_file: Annotated[Path, typer.Option()] = None):
    if log_file:
        configure_file_logging(log_file)

    main()

def configure_file_logging(log_file):
    # Attach a handler to the logger instance that logs to a file with json serialization
    # Note that it is only configured for the application logger and the library logs will
    # be ignored for the file log.
    logger.addHandler(SpecialFileHandler(log_file))
    library_logger.addHandler(SpecialFileHandler(log_file))

if __name__ == "__main__":
    typer.run(cli)
