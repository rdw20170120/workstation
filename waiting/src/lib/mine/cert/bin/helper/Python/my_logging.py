import logging
import sys

from my_exam import environment
from my_exam import ENV_PROD


def adjust_logging():
    """Adjust logging level for configured deployment environment"""
    if environment != ENV_PROD:
        logging.getLogger().setLevel(logging.DEBUG)


def configure_logging():
    # TODO: Ensure time is emitted in UTC
    logging.basicConfig(
        datefmt="%Y%m%dT%H%M%S",
        format="%(asctime)s.%(msecs)dZ PID=%(process)-5d %(name)-11s %(levelname)-5s %(message)s",
        level=logging.INFO,
    )
    logging.addLevelName(logging.CRITICAL, "FATAL")
    logging.addLevelName(logging.NOTSET, "NONE")
    logging.addLevelName(logging.WARNING, "WARN")


""" Disabled content
"""
