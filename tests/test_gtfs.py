from zipfile import ZipFile
from gtfsmerger.gtfs import GTFS


def test_to_dfs(gtfs_obj):
    assert gtfs_obj.keys() == [
        'agency',
        'stop_times',
        'stops',
        'shapes',
        'calendar_dates',
        'routes',
        'trips']
    assert gtfs_obj['stops'].iloc[:5].stop_id.tolist() == [
        u'n1502-1',
        u'n62046-1',
        u'n1520-1',
        u'n1522-1',
        u'n1510']


def test_to_zipfile(gtfs_obj):
    names = [
        'agency',
        'stop_times',
        'stops',
        'calendar_dates',
        'routes',
        'shapes',
        'trips']
    zip_f = GTFS.to_zipfile(gtfs_obj, names)
    assert isinstance(zip_f, ZipFile)
