#!/usr/bin/env python3
# logging_handler.py

import sys
import logging
import coloredlogs

# logging --
logger = logging.getLogger(__name__)
coloredlogs.install(level="DEBUG")
coloredlogs.install(level="DEBUG", logger=logger)
logger = logging.basicConfig(format="%(asctime)s - %(message)s", datefmt="%d-%b-%y %H:%M:%S", level=logging.INFO)


def info(msg):
    """standardize info; exit --"""
    logging.info("[info] %s" % msg)


def warn(msg):
    """standardize warning; exit --"""
    logging.warning("[warn] %s" % msg)


def error(msg):
    """standardize error; exit --"""
    logging.error("[err] application error %s" % msg)
    sys.exit(-1)


def debug(msg):
    """standardize debug; exit --"""
    logging.debug("[debug] %s" % msg)
