from gtfsmerger import GTFSMerger


def test_gtfs_merger(gtfs_merger):
    assert gtfs_merger.merged['stops'].iloc[:5]['stop_id'].tolist() == [
        u'0-n1502-1',
        u'0-n62046-1',
        u'0-n1520-1',
        u'0-n1522-1',
        u'0-n1510']
    z_p = gtfs_merger.get_zipfile()

    assert z_p.namelist() == [
        'agency.txt',
        'stop_times.txt',
        'stops.txt',
        'shapes.txt',
        'calendar_dates.txt',
        'routes.txt',
        'trips.txt']


def test_mod_ids(gtfs_obj):
    GTFSMerger.mod_ids(100, gtfs_obj)
    assert gtfs_obj['stops'].iloc[:5]['stop_id'].tolist() == [
        u'100-n1502-1',
        u'100-n62046-1',
        u'100-n1520-1',
        u'100-n1522-1',
        u'100-n1510']
