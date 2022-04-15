#!/usr/bin/python3
# -*- coding: UTF8 -*-

from setuptools import setup, find_packages
from sys import version_info, exit
from os import path
from mrz_trans import __version__ as version

if version_info < (3, 4):
    print("Your version is: %d.%d.%d" %
          (version_info.major, version_info.minor, version_info.micro))
    exit(1)

parent = path.abspath(path.dirname(__file__))

with open(path.join(parent, "README.rst"), 'r', errors='ignore') as readme:
    long_description = readme.read()

setup(
    name="mrz_trans",
    version=version,
    description="Machine readable zone Text transliteration",
    license="GPLv3",
    long_description=long_description,
    author='Harijaona Ravelondrina',
    author_email='hravelondrina@gmail.com',
    url="https://github.com/iharijaona/mrz_trans",
    keywords="transliterate mrz passports visas id cards td1 td2 td3 mrva mrvb icao",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Security"
    ]
)
