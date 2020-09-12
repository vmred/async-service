import pytest

from test_case import TestCase
from variables import iterations_count

iterations = [x for x in range(iterations_count)]


@pytest.mark.test_without_module
@pytest.mark.parametrize('iteration', iterations, ids=iterations)
def test_without_module_fixture(iteration):
    print('running test')
    pass


class TestClass1:
    @pytest.mark.parametrize('iteration', iterations, ids=iterations)
    def test_1_class_1(self, iteration):
        pass


class TestModule:
    @pytest.mark.parametrize('iteration', iterations, ids=iterations)
    def test_module_fixture_with_concurrency(self, iteration, verify):
        print('incrementing count')
        TestCase.count += 1
