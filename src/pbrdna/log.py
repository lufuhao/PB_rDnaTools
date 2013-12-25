#! /usr/bin/env python

__author__ = 'bbowman@pacificbiosciences.com'

import sys
import logging

LOG_FORMAT = "%(asctime)s [%(levelname)s - %(module)s] %(message)s"
TIME_FORMAT = "%Y-%m-%d %H:%M:%S"

log = logging.getLogger(__name__)

def initialize_logger(log_file=None, log_level=logging.INFO):
    # Set up a simple Stream handler
    logging.basicConfig( level=log_level,
                         format=LOG_FORMAT,
                         datefmt=TIME_FORMAT,
                         stream=sys.stdout )
    # Set a second handler for the log file
    if log_file:
        file_handler = logging.FileHandler( log_file )
        formatter = logging.Formatter( LOG_FORMAT, TIME_FORMAT )
        file_handler.setFormatter( formatter )
        file_handler.setLevel( log_level )
        log.addHandler( file_handler )