import logging
import json


class JsonFormatter(logging.Formatter):
    def format(self, record):
        return json.dumps({
            "level": record.levelname,
            "message": record.getMessage(),
            "timestamp": record.created,
            "filename": record.filename,
            "lineno": record.lineno,
            "module": record.module,
            "funcName": record.funcName,
        })

class LoggerFactory:
    __instance = None
    
    def __init__(self, name: str, level: str):
        if LoggerFactory.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            LoggerFactory.__instance = self
            self.logger = self._initialize_logger(name, level)
    
    def _initialize_logger(self, name, level):
        logger = logging.getLogger(name)
        logger.setLevel(getattr(logging, level))
        handler = logging.StreamHandler()
        handler.setFormatter(JsonFormatter())
        logger.addHandler(handler)
        return logger
    
    @staticmethod
    def get_logger(name: str = __name__, level: str = "DEBUG") -> logging.Logger:
        if LoggerFactory.__instance is None:
            LoggerFactory(name, level)
        return LoggerFactory.__instance.logger
