import pytest
from gtfsmerger import GTFSMerger
from gtfsmerger.gtfs import GTFS


@pytest.fixture(scope="module")
def gtfs_obj():
    gtfs = GTFS()
    return gtfs.to_dfs_from_fpath('tests/test_gtfs.zip')


@pytest.fixture(scope="module")
def gtfs_obj_from_bytes():
    gtfs = GTFS()
    bt = open('tests/test_gtfs.zip', 'rb').read()
    return gtfs.to_dfs_from_bytes(bt)


@pytest.fixture(scope='module')
def gtfs_merger():
    _gtfs = GTFSMerger()
    _gtfs.merge_from_fpaths([
    	'tests/test_gtfs.zip', 'tests/test_gtfs_2.zip'])
    return _gtfs

@pytest.fixture(scope='module')
def gtfs_merger_from_bytes():
    _gtfs = GTFSMerger()
    bt = open('tests/test_gtfs.zip', 'rb').read()
    bt_2 = open('tests/test_gtfs_2.zip', 'rb').read()
    _gtfs.merge_from_bytes_list([bt, bt_2])
    return _gtfs
