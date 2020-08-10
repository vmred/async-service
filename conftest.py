import pytest

from test_case import TestCase


def pytest_sessionstart(session):
    print('---------->')
    print('----------> session started')
    print('---------->')


@pytest.fixture(scope='module')
def parametrized_test_fixture():
    print('-->')
    print('module fixture called')

    yield

    print('-->')
    print('--> should be printed after all test cases')
    assert TestCase.count == 100
