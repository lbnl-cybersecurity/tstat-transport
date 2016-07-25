#! /usr/bin/env python

"""
Setup file for tstat_transport distribution.
"""

import sys
from setuptools import setup

try:
    # Use pandoc to convert .md -> .rst when uploading to pypi
    import pypandoc
    DESCRIPTION = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError, OSError):
    DESCRIPTION = open('README.md').read()

if sys.version_info[0] == 2 and sys.version_info[1] < 7:
    sys.exit('Sorry, Python < 2.7 is not supported')

setup(
    name='tstat_transport',
    version='0.4.4',
    description='Tools to send Tstat (TCP STatistic and Analysis Tool) log data to archive servers.',  # pylint: disable=line-too-long
    long_description=DESCRIPTION,
    author='Monte M. Goode',
    author_email='MMGoode@lbl.gov',
    url='https://github.com/esnet/tstat-transport',
    packages=['tstat_transport'],
    scripts=[
        'bin/tstat_send',
        'bin/tstat_cull',
    ],
    install_requires=['pika==0.10.0'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Telecommunications Industry',
        'Environment :: Console',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2',
        'Topic :: Internet',
        'Topic :: System :: Networking',
        'Topic :: Software Development :: Libraries',
    ],
)
