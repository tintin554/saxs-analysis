# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 15:53:07 2021

@author: Adam
"""


from setuptools import setup, find_packages

# versioning

MAJOR = 0
MINOR = 1
MICRO = 0
ISRELEASED = False
VERSION = f'{MAJOR}.{MINOR}.{MICRO}'

packages = find_packages()

setup(name='saxs_analysis',
      version=VERSION,
      description= 'A package with tools for reading, plotting and analysing SAXS data from multiple sources',
      author= 'Adam Milsom'
      author_email= 'axm1535@student.bham.ac.uk',
      license= 'MIT',
      packages= packages,
      setup_requires= ['numpy','matplotlib','h5py'],
      python_requires= >=3.1
      
      )