import pytest
import time
from roku_laser import RokuMonitor

DELAY = 1

@pytest.fixture(scope='module')
def rm(request):
    return RokuMonitor()

def test_current_app(rm):
    assert type(rm.current_app) == str

def test_home(rm):
    rm.home()
    time.sleep(DELAY)

    assert rm.current_app == 'Roku'

    netflix = rm.roku['Netflix']
    netflix.launch()
    time.sleep(DELAY)

    assert rm.current_app == 'Netflix'

    rm.home()
    time.sleep(DELAY)

    assert rm.current_app == 'Roku'
