import pytest

from async_service import AsyncService
from test_case import TestCase

iterations = [x for x in range(100)]


@pytest.mark.asyncio_cooperative
@pytest.mark.parametrize('iteration', iterations, ids=iterations)
async def test_a(iteration):
    service = AsyncService()
    await service.is_processed(iteration, timeout=5)
    assert service.result_url == 'https://google.com'


@pytest.mark.parametrize('iteration', iterations, ids=iterations)
def test_pytest_concurrent(iteration):
    # service = AsyncService()
    # service.wait_is_processed(iteration, timeout=5)
    # assert service.result_url == 'https://google.com'
    pass


@pytest.mark.test_module
@pytest.mark.parametrize('iteration', iterations, ids=iterations)
def test_module_fixture_with_concurrency(iteration, parametrized_test_fixture):
    TestCase.count += 1
    print(iteration)