import logging

# Creating a logger instance with the same name as the package
# and attach a NullHandler instance to this logger, so that
# Python won't default to using the LasResort handler.
logging.getLogger(__name__).addHandler(logging.NullHandler())