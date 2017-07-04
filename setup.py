#!/usr/bin/env python

import os
import sys

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages


# if sys.argv[-1] == 'publish':
#     os.system('python setup.py sdist upload')
#     sys.exit()


setup(
    name='gtfsmerger',
    version='0.1.5',
    description='Merge multiple GTFS files into one',
    author='Door2Door GmbH',
    author_email='chenghsun@door2door.io',
    url='https://github.com/door2door-io/gtfs-merger',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['pandas'],
    license='MIT',
    zip_safe=False,
    keywords='gtfsmerger',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ]
)
