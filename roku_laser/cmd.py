import sys
import argparse
import logging
import time

from .roku import RokuMonitor

logging.basicConfig(level=logging.DEBUG)

log = logging.getLogger('cmd')

def go():
    rm = RokuMonitor()
    log.debug('Connected.')
    rm.start()

def main():
    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    while True:
        try:
            go()
        except KeyboardInterrupt:
            log.info('Exiting, keyboard interrupt.')
            sys.exit()
        except OSError:
            log.error('Can not connect to network')
            time.sleep(10)
