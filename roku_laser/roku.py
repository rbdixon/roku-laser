import roku
import schedule
import time
import logging

from datetime import datetime

log = logging.getLogger('RokuMonitor')

class RokuMonitor():

    def __init__(self):
        self.roku = None
        self.find_roku()

    def find_roku(self, tries=10):
        attempts = 0
        while self.roku is None and attempts < tries:
            log.debug('Looking for Roku, attempt {0}'.format(attempts + 1))
            attempts += 1
            found = roku.Roku.discover()
            if len(found) > 0:
                log.debug('Found {0} Roku'.format(len(found)))
                self.roku = found[0]

        if self.roku is None:
            raise Exception('Could not find Roku')

    def check(self):
        if self.roku.current_app.name != 'Roku':
            if datetime.now().weekday() < 5:
                log.info('Sending Roku back to home screen.')
                self.roku.home()

    def start(self):
        schedule.every(5).seconds.do(self.check)

        while True:
            schedule.run_pending()
            time.sleep(1)

