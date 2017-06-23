from gtfsmerger import GTFSMerger
import pandas as pd
from pandas.util import testing as tm

import pytest


def test_gtfs_merger(gtfs_merger):
    assert gtfs_merger.merged['stops'].iloc[:5]['stop_id'].tolist() == [
        u'0-n1502-1',
        u'0-n62046-1',
        u'0-n1520-1',
        u'0-n1522-1',
        u'0-n1510']

    assert gtfs_merger.merged['stops'].iloc[:4]['parent_station'].tolist() == [
        '0-n1502', '0-n62046', '0-n1520', '0-n1522']

    assert pd.isnull(gtfs_merger.merged['stops'].iloc[5][
        'parent_station'])

    z_p = gtfs_merger.get_zipfile()

    assert set(z_p.namelist()) == set([
        'agency.txt',
        'stop_times.txt',
        'stops.txt',
        'shapes.txt',
        'calendar_dates.txt',
        'routes.txt',
        'trips.txt'])


def test_gtfs_merger_from_bytes(gtfs_merger_from_bytes):
    assert gtfs_merger_from_bytes.merged[
        'stops'].iloc[:5]['stop_id'].tolist() == [
            u'0-n1502-1',
            u'0-n62046-1',
            u'0-n1520-1',
            u'0-n1522-1',
            u'0-n1510']

    assert gtfs_merger_from_bytes.merged['stops'].iloc[:4][
        'parent_station'].tolist() == [
            '0-n1502', '0-n62046', '0-n1520', '0-n1522']

    assert pd.isnull(gtfs_merger_from_bytes.merged['stops'].iloc[5][
        'parent_station'])

    z_p = gtfs_merger_from_bytes.get_zipfile()

    assert set(z_p.namelist()) == set([
        'agency.txt',
        'stop_times.txt',
        'stops.txt',
        'shapes.txt',
        'calendar_dates.txt',
        'routes.txt',
        'trips.txt'])


def test_mod_ids(gtfs_obj):
    GTFSMerger.mod_ids(100, gtfs_obj)
    assert gtfs_obj['stops'].iloc[:5]['stop_id'].tolist() == [
        u'100-n1502-1',
        u'100-n62046-1',
        u'100-n1520-1',
        u'100-n1522-1',
        u'100-n1510']


@pytest.mark.parametrize('tag,in_series,out_series', [
    (0, pd.Series(), pd.Series()),
    (0, pd.Series({0: 'a', 1: 'b', 3: 'd'}, index=[0, 1, 2, 3]),
     pd.Series({0: '0-a', 1: '0-b', 3: '0-d'}, index=[0, 1, 2, 3])),
    (0, pd.Series({0: 1, 1: 2, 3: 4}, index=[0, 1, 2, 3]),
     pd.Series({0: '0-1.0', 1: '0-2.0', 3: '0-4.0'}, index=[0, 1, 2, 3])),
])
def test_tag_series(tag, in_series, out_series):
    result = GTFSMerger.tag_series(tag, in_series)
    print(in_series.dtypes)
    tm.assert_series_equal(result, out_series)
