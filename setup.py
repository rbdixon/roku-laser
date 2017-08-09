#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='roku_laser',
    install_requires = [
        'python-roku',
        'schedule',
    ],
    version='1.0',
    description='Kick the kids off of the Roku during weeknights',
    author='Brad Dixon',
    author_email='rbdixon@gmail.com',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'roku-laser = roku_laser.cmd:main',
        ]
    },
)
