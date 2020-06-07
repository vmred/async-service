import pytest


@pytest.fixture(scope='session', autouse=True)
def fix():
    print('---------->')
    print('----------> session scope fixture executed')
    print('----------> \n')
