import pytest
from gtfsmerger import GTFSMerger
from gtfsmerger.gtfs import GTFS


@pytest.fixture(scope="module")
def gtfs_obj():
    gtfs = GTFS()
    with open('tests/test_gtfs.zip') as test_f:
        return gtfs.to_dfs(test_f)


@pytest.fixture(scope='module')
def gtfs_merger():
    f_a = open('tests/test_gtfs.zip')
    f_b = open('tests/test_gtfs_2.zip')
    return GTFSMerger(f_a, f_b)
