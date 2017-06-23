import pandas as pd
from gtfsmerger.gtfs import GTFS


class GTFSMerger(object):

    ref_columns = GTFS.ref_columns

    def __init__(self):
        self.merged = None
        self.gtfs_objs = None
        self.gtfs_tables = set()

    def merge_from_fpaths(self, fpaths):
        self.merged_gtfs_objs(GTFS.to_dfs_from_fpath, fpaths)

    def merge_from_bytes_list(self, bytes_objs):
        self.merged_gtfs_objs(GTFS.to_dfs_from_bytes, bytes_objs)

    def merged_gtfs_objs(self, to_dfs, objs):
        self.gtfs_objs = [to_dfs(obj) for obj in objs]
        for cnt, gtfs in enumerate(self.gtfs_objs):
            self.gtfs_tables.update(gtfs.keys())
            self.mod_ids(cnt, gtfs)
        self.merged = self.merge(self.gtfs_objs)

    def mod_ids(self, cnt, gtfs):
        for ref in self.gtfs_tables:
            for col in self.ref_columns:
                try:
                    gtfs[ref][col] = self.tag_series(cnt, gtfs[ref][col])
                except KeyError:
                    pass

    @staticmethod
    def tag_series(tag, series):
        return series.apply(
            lambda x: '{}-{}'.format(tag, x) if not pd.isnull(x) else x
        )

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
