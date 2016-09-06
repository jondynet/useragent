# -*- coding: utf-8 -*-
""" useragent setup.py script """

# system
from distutils.core import setup
from setuptools import setup, find_packages

setup(
    name='useragent',
    version='0.1.1',
    author='zhangdi',
    author_email='jondynet@gmail.com',
    packages = find_packages(),
    include_package_data=True,
    url='',
    license="MIT licensed. See LICENSE.txt in the source distribution.",
    description=''
)
