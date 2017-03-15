from zipfile import ZipFile
from io import StringIO
from io import BytesIO

import pandas as pd


class GTFS(object):

    @staticmethod
    def to_dfs_from_fpath(fpath):
        zip_ref = ZipFile(fpath)
        return GTFS.zip_obj_to_dfs(zip_ref)

    @staticmethod
    def to_dfs_from_bytes(bytes_obj):
        zip_ref = ZipFile(BytesIO(bytes_obj))
        return GTFS.zip_obj_to_dfs(zip_ref)

    @staticmethod
    def zip_obj_to_dfs(zip_obj):
        gtfs_obj = {}
        for filename in zip_obj.namelist():
            filelabel = filename.replace('.txt', '')
            gtfs_obj[filelabel] = pd.read_csv(zip_obj.open(filename),
                                              encoding='utf-8-sig',
                                              dtype=str)
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
