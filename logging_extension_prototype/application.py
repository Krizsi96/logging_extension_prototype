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

logger = getLogger(__name__)

def main():
    logger.info("Hello from logging-extension-prototype!")

    for i in range(10):
        logger.debug(f"iteration: {i}")
        time_keeper()
        data_monitor()

def cli(log_file: Annotated[Path, typer.Option()] = None):
    configure_console_logging()
    if log_file:
        configure_file_logging(log_file)

    main()

def configure_file_logging(log_file):
    # Attach a handler to the logger instance that logs to a file with json serialization
    special_file_handler = SpecialFileHandler(log_file)
    logger.addHandler(special_file_handler)
    library_logger.addHandler(special_file_handler)

def configure_console_logging():
    # Define the level of logging on console for logs coming from the application
    application_console_logging = logging.StreamHandler()
    application_console_logging.setLevel(logging.DEBUG)
    logger.addHandler(application_console_logging)
    logger.setLevel(logging.DEBUG)

    # Define the level of logging on console for logs coming from the library
    library_console_logging = logging.StreamHandler()
    library_console_logging.setLevel(logging.INFO)
    library_logger.addHandler(library_console_logging)
    library_logger.setLevel(logging.DEBUG)

if __name__ == "__main__":
    typer.run(cli)
