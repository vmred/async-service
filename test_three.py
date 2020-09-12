import json
import pytest
import random

from filelock import FileLock

from test_async_service import iterations
from test_case import TestCase
from variables import iterations_count


def random_num():
    TestCase.count += 1
    return TestCase.count


@pytest.fixture(scope="session")
def get_random_num(tmp_path_factory, worker_id):
    if not worker_id:
        # not executing in with multiple workers, just produce the data and let
        # pytest's fixture caching do its job
        return random_num()

    # get the temp directory shared by all workers
    root_tmp_dir = tmp_path_factory.getbasetemp().parent

    fn = root_tmp_dir / "data.json"
    with FileLock(str(fn) + ".lock"):
        if fn.is_file():
            data = json.loads(fn.read_text())
        else:
            data = random_num()
            fn.write_text(json.dumps(data))
    return data


# @pytest.mark.parametrize('iteration', iterations, ids=iterations)
# def test_module_fixture_with_concurrency(iteration, get_random_num):
#     assert TestCase.count == iterations_count
