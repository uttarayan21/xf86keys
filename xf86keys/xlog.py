import os
import sys
import logging
import datetime


def log_it(string):
    """Show messages to tty if run from terminal or store them to logfile"""
    log_file = os.path.expanduser('~') + '/.cache/xf86keys.log'
    readable_timestamp = datetime.datetime.fromtimestamp(
        1530238401).isoformat()
    if sys.stdin.isatty():
        print(readable_timestamp + ' ' + string + '\n')
    else:
        with open(log_file, 'a+') as log:
            log.write(readable_timestamp + ' ' + string + '\n')
