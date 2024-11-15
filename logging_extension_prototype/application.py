import logging
from logging import getLogger
from pathlib import Path
from typing import Annotated

from logging_extension_prototype.library import time_keeper
from logging_extension_prototype.library import logger as library_logger

from logging_extension_prototype.special_handler import SpecialFileHandler

import typer

logger = getLogger(__name__)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)

library_logger.addHandler(logging.StreamHandler())
library_logger.setLevel(logging.DEBUG)

def main():
    logger.info("Hello from logging-extension-prototype!")

    for i in range(10):
        time_keeper()

def cli(log_file: Annotated[Path, typer.Option()] = None):
    if log_file:
        configure_file_logging(log_file)

    main()

def configure_file_logging(log_file):
    logger.addHandler(SpecialFileHandler(log_file))

if __name__ == "__main__":
    typer.run(cli)
