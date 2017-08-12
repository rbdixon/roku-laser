import pytest
from roku_laser import RokuMonitor

@pytest.fixture(scope='session')
def rm(request):
    return RokuMonitor(mock=True)
