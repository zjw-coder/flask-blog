#!/usr/bin/env python
# encoding: utf-8
"""
:author: lixing
:file: setup.py
:time: 2020/5/17 20:38
:file_desc: 
"""

from setuptools import find_packages, setup

setup(
    name='flaskr',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
)
