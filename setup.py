# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('README.md') as f:
    README = f.read()

with open('LICENSE') as f:
    LICENSE = f.read()

setup(
    name='raspberry-resources',
    version='0.1.0',
    description='Raspberry Resources',
    long_description=README,
    author='Benjamin Schmitt',
    author_email='',
    url='https://github.com/foxdb/raspberry-resources',
    license=LICENSE,
    packages=find_packages(exclude=('tests', 'docs'))
)
