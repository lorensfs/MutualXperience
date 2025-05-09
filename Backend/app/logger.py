import logging
import os

from app.core.config import settings

def get_logger(logger_name: str):
    logger = logging.getLogger(logger_name)

    if not logger.hasHandlers():
        logger.setLevel(getattr(logging, settings.LOG_LEVEL, logging.INFO))

        # Create a console handler for stdout
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(logging.Formatter(settings.LOG_FORMAT))

        logger.addHandler(console_handler)

    return logger

