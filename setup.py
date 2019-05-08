#!/usr/bin/env python

import os
from setuptools import setup, find_packages

from pytest_hue import __prog__, __version__, __author__, __email__, __description__, __keywords__, __license__, __url__

setup(
    name=__prog__,
    version=__version__,
    author=__author__,
    author_email=__email__,
    description=__description__,
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
    license=__license__,
    url=__url__,
    keywords=__keywords__,
    classifiers=[
        'Framework :: Pytest',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'License :: OSI Approved :: GNU General Public License (GPL)'
    ],
    packages=find_packages(exclude=['tests*']),
    install_requires=[
        'pytest>=3.6',
        'six>=1.0.0'
    ],
    extras_require={
        'test': [
            'pytest-xdist>=1.26.0'
        ]
    },
    entry_points={
        'pytest11': [
            'pytest_hue = pytest_hue._plugin',
        ]
    },
)