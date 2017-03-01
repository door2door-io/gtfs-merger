gtfs-merger ![build status](https://travis-ci.com/door2door-io/gtfs-merger.svg?token=jAe2MpoP1Smhms3S1hzy&branch=master)
===========
A Python package to merge multiple GTFS files into one

## Installation
```shell
python setup.py install
```

## Usage example

Use this module to merge two GTFS files
```python
>>> from gtfsmerger import GTFSMerger
>>> with open('gtfs1.zip') as fa, open('gtfs2.zip') as fb:
>>>    merged_gtfs = GTFSMerger(fa, fb)
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
['agency', 'stop_times', 'stops', 'shapes', 'calendar_dates', 'routes', 'trips']
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
0             0          n1502                   0
1             0         n62046                   0
2             0          n1520                   0
3             0          n1522                   0
4             1            NaN                   0
```

## Development
Note this package currently supports only Python2.7

### Setup
```shell
virtualenv -p python2 venv
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
