from zipfile import ZipFile
from io import StringIO
from io import BytesIO

import pandas as pd


class GTFS(object):

    @staticmethod
    def to_dfs(gtfs_data):
        gtfs_obj = {}
        zip_ref = ZipFile(gtfs_data.name)

        for filename in zip_ref.namelist():
            filelabel = filename.replace('.txt', '')
            gtfs_obj[filelabel] = pd.read_csv(zip_ref.open(filename),
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
