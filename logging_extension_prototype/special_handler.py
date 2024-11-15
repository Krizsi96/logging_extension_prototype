import logging
import json

class SpecialFileHandler(logging.Handler):
    def __init__(self, filename):
        super().__init__()
        self.stream = None
        self.filename = filename
        self._open()

    def _open(self):
        if self.stream is None:
            self.stream = open(self.filename, 'w')

    def emit(self, record):
        if self.stream is None:
            self._open()

        try:
            log_entry = self.serialize(record)

            self.stream.write(log_entry + '\n')
            self.flush()
        except Exception:
            self.handleError(record)

    def serialize(self, record):
        return json.dumps({
            'time': record.created,
            'level': record.levelname,
            'message': record.getMessage(),
        })

    def close(self):
        if self.stream and not self.stream.closed:
            self.stream.write(json.dumps({
                'time': '',
                'level': 'INFO',
                'message': 'Logging finished',
            }) + '\n')
            self.flush()
            self.stream.close()
            self.stream = None
        super().close()

    def flush(self):
        if self.stream and not self.stream.closed:
            self.stream.flush()