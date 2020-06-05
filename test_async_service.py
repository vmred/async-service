import pytest

from async_service import AsyncService

iterations = [x for x in range(1000)]


@pytest.mark.asyncio_cooperative
@pytest.mark.parametrize('iteration', iterations, ids=iterations)
async def test_asyncio_cooperative(iteration):
    service = AsyncService()
    # assert service.wait_is_processed(iteration=iteration, timeout=5) == 'https://google.com'
    await service.is_processed(iteration, timeout=5)
    assert service.result_url == 'https://google.com'


@pytest.mark.parametrize('iteration', iterations, ids=iterations)
def test_pytest_concurrent(iteration):
    service = AsyncService()
    # assert service.wait_is_processed(iteration=iteration, timeout=5) == 'https://google.com'
    service.wait_is_processed(iteration, timeout=5)
    assert service.result_url == 'https://google.com'
