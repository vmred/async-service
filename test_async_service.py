import pytest

from async_service import AsyncService

iterations = [x for x in range(5)]


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


@pytest.mark.test_one
@pytest.mark.parametrize('iteration', iterations, ids=iterations)
def test_one(iteration):
    pass


@pytest.mark.test_two
@pytest.mark.parametrize('iteration', iterations, ids=iterations)
def test_two(iteration):
    pass
