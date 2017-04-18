gtfs-merger ![build status](https://travis-ci.com/door2door-io/gtfs-merger.svg?token=jAe2MpoP1Smhms3S1hzy&branch=master)
===========
A Python package to merge multiple GTFS files into one

## Installation
```shell
pip install gtfsmerger
```

## Usage example

Use this module to merge two GTFS files
```python
>>> from gtfsmerger import GTFSMerger
>>> gtfs_merger = GTFSMerger()
>>> gtfs_merger.merge_from_fpaths(['tests/test_gtfs.zip', 'tests/test_gtfs_2.zip'])
```
Can also use zipfile bytes as input, this is useful for [Boto3](http://boto3.readthedocs.io/en/latest/reference/services/s3.html#S3.Client.get_object)
```python
>>> merged_gtfs = GTFSMerger()
>>> f_1 = open('tests/test_gtfs.zip', 'rb').read()
>>> f_2 = open('tests/test_gtfs_2.zip', 'rb').read()
>>> merged_gtfs.merge_from_bytes_list([f_1, f_2])
```

To write the merged result to a ZIP file
```python
>>> merged_gtfs.get_zipfile("./merged_gtfs.zip")
```

The class instance also contains a `merged` attribute,
that is a dictionary of the merged GTFS Pandas DataFrames.

To list the GTFS Pandas DataFrames
```python
>>> merged_gtfs.merged.keys()
dict_keys(['stops', 'stop_times', 'calendar_dates', 'shapes', 'agency', 'routes', 'trips'])
```

To access the `stops` GTFS Pandas Dataframe
```python
>>> merged_gtfs.merged['stops'].head()
      stop_id    stop_name  stop_desc   stop_lat    stop_lon stop_url  \
0   0-n1502-1      美感ホール入口  掛川市内循環南回り  34.767448  138.010986      NaN
1  0-n62046-1  中東遠総合医療センター  掛川市内循環南回り  34.757321  137.998436      NaN
2   0-n1520-1       中央小学校前  掛川市内循環南回り  34.770991  138.005292      NaN
3   0-n1522-1      労金掛川支店前  掛川市内循環南回り  34.770798  138.008737      NaN
4     0-n1510      下俣南二丁目西  掛川市内循環南回り  34.762361  138.001036      NaN

  location_type parent_station wheelchair_boarding
0             0        0-n1502                   0
1             0       0-n62046                   0
2             0        0-n1520                   0
3             0        0-n1522                   0
4             1            NaN                   0

```

## Development
Note this package currently supports only Python3

### Setup
```shell
virtualenv -p python3 venv
source venv/bin/activate
```

### Install the dependency
```shell
make install
```

### Run tests
```shell
make test
```
