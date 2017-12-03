#!/usr/bin/env python

from setuptools import setup, find_packages


setup(
    name='advent',
    version='2017',
    description='Advent of Code solutions',
    license='BSD',

    author='Jeff Forcier',
    author_email='jeff@bitprophet.org',

    packages=find_packages(),

    classifiers=[
        'Environment :: Console',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
