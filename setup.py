#!/usr/bin/env python3
from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()


def read_requirements():
    with open("requirements.txt") as f:
        return f.read().splitlines()
requirements = read_requirements()

setup(name='nslookup',
      version='1.1.1',
      description='Sensible high-level DNS lookups in Python, using DNSpython resolver',
      long_description=readme,
      long_description_content_type='text/markdown',
      url='https://github.com/wesinator/pynslookup',
      author='wesinator',
      keywords='dns',
      packages=find_packages(exclude=(["tests", "docs"])),
      install_requires=requirements,
      classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
      ],
      zip_safe=True)
