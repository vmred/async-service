import pytest

from test_case import TestCase
from variables import iterations_count


def pytest_sessionstart(session):
    print('---------->')
    print('----------> session started')
    print('---------->')


@pytest.yield_fixture(scope='module')
def parametrized_test_fixture():
    print('-->')
    print('module fixture called')

    yield True

    print('-->')
    print('--> should be printed after all test cases')
    assert TestCase.count == iterations_count
