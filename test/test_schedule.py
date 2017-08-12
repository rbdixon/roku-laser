import pytest
import itertools

from datetime import datetime

PM = 12

@pytest.mark.parametrize('now, app, skip', [
    # Weekdays
    [datetime(2017, 8, 2, 3+PM, 0), 'Netflix', True],
    [datetime(2017, 8, 2, 9+PM, 0), 'Netflix', False],
    [datetime(2017, 8, 2, 3+PM, 0), 'Roku', False],
    [datetime(2017, 8, 2, 9+PM, 0), 'Roku', False],
    # Saturday
    [datetime(2017, 8, 5, 3+PM, 0), 'Netflix', False],
    [datetime(2017, 8, 5, 3+PM, 0), 'Roku', False],
])
def test_schedule(rm, now, app, skip):
    rm._home = False
    rm._current_app = app
    rm._now = now

    rm.check()

    assert rm._home  == skip
