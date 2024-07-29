#!/usr/bin/env python3
# coding: utf-8

# Copyright (c) Colav.
# Distributed under the terms of the Modified BSD License.

# -----------------------------------------------------------------------------
# Minimal Python version sanity check (from IPython)
# -----------------------------------------------------------------------------

# See https://stackoverflow.com/a/26737258/2268280
# sudo pip3 install twine
# python3 setup.py sdist bdist_wheel
# twine upload dist/*
# For test purposes
# twine upload --repository-url https://test.pypi.org/legacy/ dist/*

from __future__ import print_function
from setuptools import setup, find_packages

import os
import sys
import codecs


v = sys.version_info


def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")


shell = False
if os.name in ('nt', 'dos'):
    shell = True
    warning = "WARNING: Windows is not officially supported"
    print(warning, file=sys.stderr)


def main():
    setup(
        # Application name:
        name="Kahi",

        # Version number (initial):
        version=get_version('kahi/_version.py'),

        # Application author details:
        author="Colav",
        author_email="colav@udea.edu.co",

        # Packages
        packages=find_packages(exclude=['tests']),

        # Include additional files into the package
        include_package_data=True,

        # Details
        url="https://github.com/colav/Kahi",
        scripts=['bin/kahi_run','bin/kahi_generate'],

        license="BSD",

        description="ETL (Extract, Transform and Load) for bibliographic data using an advance data workflow",

        long_description=open("README.md").read(),

        long_description_content_type="text/markdown",

        # Dependent packages (distributions)
        install_requires=[
            "pyyaml",
            "pymongo"
        ],
        extras_require={
            'all': [
                'kahi_doaj_sources',
                'kahi_minciencias_opendata_affiliations',
                'kahi_minciencias_opendata_person',
                'kahi_openalex_affiliations',
                'kahi_openalex_person',
                'kahi_openalex_sources',
                'kahi_openalex_subjects',
                'kahi_openalex_works',
                'kahi_ranking_udea_works',
                'kahi_ror_affiliations',
                'kahi_scholar_works',
                'kahi_scienti_affiliations',
                'kahi_scienti_person',
                'kahi_scienti_sources',
                'kahi_scholar_works',
                'kahi_scimago_sources',
                'kahi_scopus_works',
                'kahi_staff_udea_affiliations',
                'kahi_staff_udea_person',
                'kahi_wos_works'
            ]
        }
    )


if __name__ == "__main__":
    main()
