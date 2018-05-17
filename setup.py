# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

setup(
    name='sample',
    version='0.0.1',
    description='Trabajo Verificacion y Desarrollo',
    long_description=readme,
    author='Bosco Vallejo',
    author_email='juan.vallejo@u-tad.live.com',
    packages=find_packages(exclude=('tests', 'docs'))
)