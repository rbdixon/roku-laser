import roku
import schedule
import time
import logging

from datetime import datetime

log = logging.getLogger('RokuMonitor')

PM8 = 8 + 12

class RokuMonitor():

    def __init__(self, mock=False):
        self.roku = None

        # For testing
        self.mock = mock
        self._now = None
        self._current_app = None
        self._home = False

        if not self.mock:
            self.find_roku()

    @property
    def now(self):
        return self._now or datetime.now()

    @property
    def current_app(self):
        return self._current_app or self.roku.current_app.name

    def home(self):
        if not self.mock:
            self.roku.home()
        else:
            self._home = True

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
        if self.current_app != 'Roku':
            if self.now.weekday() < 5 and self.now.hour < PM8:
                log.info('Sending Roku back to home screen.')
                self.home()

    def start(self):
        schedule.every(5).seconds.do(self.check)

        while True:
            schedule.run_pending()
            time.sleep(1)

