#!/usr/bin/env python

from setuptools import setup, find_packages
from upconvert import version

packages = ['upconvert.' + p for p in find_packages('upconvert', exclude=['test', 'test*', '*.t'])]
packages.append('upconvert')

setup(
    name='python-upconvert',
    maintainer='Upverter Inc.',
    maintainer_email='opensource@upverter.com',
    version=version(),
    description='Upconvert library',
    license='Apache 2.0',
    url='https://github.com/upverter/schematic-file-converter',
    packages=packages,
)
