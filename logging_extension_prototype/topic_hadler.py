import logging
import json
from logging_extension_prototype.special_handler import SpecialFileHandler

class TopicLogger:
    def __init__(self, name: str, logger: logging.Logger):
        self.name = name
        self.logger = logger
        self.stream = None

    def write(self, data: dict):
        for handler in self.logger.handlers:
            if isinstance(handler, SpecialFileHandler):
                self.stream = handler.stream

        if self.stream is not None:
            log_entry = json.dumps({
                'time': '',
                'topic': self.name,
                'data': data,
            })
            self.stream.write(log_entry + '\n')
            self._flush()

    def _flush(self):
        if self.stream and not self.stream.closed:
            self.stream.flush()
        self.stream = None