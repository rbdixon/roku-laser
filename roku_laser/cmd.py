import sys
import argparse
import logging
import time

from .roku import RokuMonitor

log = logging.getLogger('cmd')

def go():
    rm = RokuMonitor()
    log.debug('Connected.')
    rm.start()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', action='count', default=0, help='Increase verbosity')
    args = parser.parse_args()

    if args.v > 0:
        logging.basicConfig(level=logging.DEBUG)        

    while True:
        try:
            go()
        except KeyboardInterrupt:
            log.info('Exiting, keyboard interrupt.')
            sys.exit()
        except OSError:
            log.error('Can not connect to network')
            time.sleep(10)
