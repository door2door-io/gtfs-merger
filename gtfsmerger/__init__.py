import pandas as pd
from gtfsmerger.gtfs import GTFS


class GTFSMerger(object):

    ref_id = {
        'agency': ['agency_id'],
        'calendar': ['service_id'],
        'calendar_dates': ['service_id'],
        'stop_times': ['trip_id', 'stop_id'],
        'stops': ['stop_id'],
        'shape': ['shape_id'],
        'trips': ['route_id', 'trip_id', 'service_id'],
        'transfer': ['from_stop_id', 'to_stop_id'],
        'routes': ['route_id', 'agency_id'],
        'fare_rule': ['fare_id', 'route_id'],
        'fare_attribute': ['fare_id'],
        'frequency': ['trip_id']
    }

    def __init__(self, *files):
        self.gtfs_objs = [GTFS().to_dfs(gtfs) for gtfs in files]

        tables = []
        for obj in self.gtfs_objs:
            tables += obj.keys()
        self.gtfs_tables = set(tables)
        for cnt, gtfs in enumerate(self.gtfs_objs):
            self.mod_ids(cnt, gtfs)
        self.merged = self.merge(self.gtfs_objs)

    @classmethod
    def mod_ids(cls, cnt, gtfs):
        tag = str(cnt) + '-'
        for ref in cls.ref_id:
            columns = cls.ref_id[ref]
            for col in columns:
                try:
                    gtfs[ref][col] = gtfs[ref][col].apply(lambda x: tag + x)
                except KeyError:
                    pass

    def merge(self, gtfs_objs):
        merged_gtfs = {}
        for ref in self.gtfs_tables:
            dfs = []
            for gtfs in gtfs_objs:
                try:
                    dfs.append(gtfs[ref])
                except KeyError:
                    pass
            merged_gtfs[ref] = pd.concat(dfs)
        return merged_gtfs

    def get_zipfile(self, fpath=None):
        if not fpath:
            return GTFS().to_zipfile(self.merged, self.gtfs_tables)
        else:
            return GTFS().to_zipfile(
                self.merged, self.gtfs_tables, fpath=fpath)
