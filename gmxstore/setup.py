#!/usr/bin/env python

from setuptools import setup, find_packages

__version__ = '1.0'

__build__ = ''

setup(name='gmxstore',
      version=__version__ + __build__,
      description='Grocermax Android app store(Grocermax Play Store)',
      author='Location Labs',
      author_email='info@locationlabs.com',
      url='http://www.locationlabs.com',
      packages=find_packages(exclude=['*.tests']),
      setup_requires=[
          'nose>=1.0',
      ],
      install_requires=[
          'Flask>=0.8',
          'timber>=1.5',
          'uWSGI>=1.9.20',
      ],
      tests_require=[
      ],
      test_suite='gmxstore.tests',
      entry_points={
          'console_scripts': [
              'development = gmxstore.development:main',
          ]
      },
      )
