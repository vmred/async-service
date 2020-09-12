import pytest

from test_case import TestCase
from variables import iterations_count

import logging

logger = logging.getLogger('foo')


def pytest_sessionstart(session):
    print('---------->')
    print('----------> session started')
    print('---------->')


@pytest.fixture(scope='module')
def verify():
    yield
    print('\n--->')
    print('teardown')
    assert TestCase.count == iterations_count
