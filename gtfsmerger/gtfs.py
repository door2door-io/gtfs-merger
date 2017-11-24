from zipfile import ZipFile
from io import StringIO
from io import BytesIO

import pandas as pd


class GTFS(object):

    ref_columns = {'agency_id', 'service_id', 'fare_id', 'route_id',
                   'trip_id', 'shape_id', 'stop_id', 'parent_station',
                   'from_stop_id', 'to_stop_id'}

    @classmethod
    def to_dfs_from_fpath(cls, fpath):
        zip_ref = ZipFile(fpath)
        return cls.zip_obj_to_dfs(zip_ref)

    @classmethod
    def to_dfs_from_bytes(cls, bytes_obj):
        zip_ref = ZipFile(BytesIO(bytes_obj))
        return cls.zip_obj_to_dfs(zip_ref)

    @classmethod
    def zip_obj_to_dfs(cls, zip_obj):
        gtfs_obj = {}
        # Set dtype to string for reference columns.
        dtype = {c: str for c in cls.ref_columns}
        for filename in zip_obj.namelist():
            if not filename.endswith('.txt'):
                continue
            filelabel = filename[:-4]
            gtfs_obj[filelabel] = pd.read_csv(zip_obj.open(filename),
                                              encoding='utf-8-sig',
                                              dtype=dtype)
        return gtfs_obj

    @staticmethod
    def to_zipfile(gtfs_obj, tables, fpath=None):
        if not fpath:
            zip_buf = BytesIO()
            zip_archive = ZipFile(zip_buf, mode='w')
        else:
            zip_archive = ZipFile(fpath, mode='w')

        for table_name in tables:
            buff = StringIO()
            gtfs_obj[table_name].to_csv(buff, encoding='utf-8-sig')
            zip_archive.writestr(table_name + '.txt', buff.getvalue())

        zip_archive.close()
        return zip_archive
