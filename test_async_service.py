import pytest

from async_service import AsyncService
from test_case import TestCase
from variables import iterations_count

iterations = [x for x in range(iterations_count)]


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


@pytest.mark.test_without_module
@pytest.mark.parametrize('iteration', iterations, ids=iterations)
def test_without_module_fixture(iteration):
    pass


# @pytest.fixture(autouse=True)
# def autofix(request):
#     marker_names = {m.name for m in request.node.iter_markers()}
#     print(marker_names)
#     # if 'sometimes_please' in marker_names:
#     #     request.getfixturevalue('sometimes_fixture')
#     # if 'but_also_skip_ok' in marker_names:
#     #     pytest.skip('plz skip!')
