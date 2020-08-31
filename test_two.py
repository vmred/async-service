from test_async_service import test_without_module_fixture, iterations
from test_async_service import TestClass1


test_without_module_fixture(iterations)


class TestTwo:
    TestClass1.test_1_class_1(None, iterations)