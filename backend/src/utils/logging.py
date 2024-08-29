import logging
import json

from src.config import settings

class JsonFormatter(logging.Formatter):
    """
    Custom formatter to output logs in JSON format.
    """

    def format(self, record):
        log_record = {
            'timestamp': self.formatTime(record, self.datefmt),
            'level': record.levelname,
            'name': record.name,
            'message': record.getMessage(),
        }

        # Add exception information if available
        if record.exc_info:
            log_record['exception'] = self.formatException(record.exc_info)

        return json.dumps(log_record)

class Logger:
    """
    A custom logger class that uses the logging library, 
    reads the log level from environment variables,
    and outputs logs in JSON format.
    """

    def __init__(self, name=__name__, logger_instance=None):
        self.logger = logger_instance or logging.getLogger(name)
        self.logger.setLevel(self._get_log_level())

        formatter = JsonFormatter()  # Use the custom JSON formatter

        # Create a handler for writing logs to a file
        file_handler = logging.FileHandler('task_manager.log')
        file_handler.setLevel(self._get_log_level())
        file_handler.setFormatter(formatter)

        self.logger.addHandler(file_handler)

    def _get_log_level(self):
        """
        Gets the log level from environment variables.
        Defaults to INFO if not set or invalid.
        """
        log_level = settings.LOG_LEVEL
        if log_level:
            try:
                return getattr(logging, log_level.upper())
            except AttributeError:
                print(f"Invalid log level '{log_level}' in environment variables. Defaulting to INFO.")
        return logging.INFO

    def debug(self, msg, *args, **kwargs):
        self.logger.debug(msg, *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        self.logger.info(msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        self.logger.warning(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        self.logger.error(msg, *args, **kwargs)

    def critical(self, msg, *args, **kwargs):
        self.logger.critical(msg, *args, **kwargs)

# Create an instance of the logger
logger = Logger()
