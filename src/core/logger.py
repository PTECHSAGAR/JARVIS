"""
logger.py - Provides centralized logging utilities.
"""
import logging

def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    # TODO: Configure logger format and handlers.
    return logger
