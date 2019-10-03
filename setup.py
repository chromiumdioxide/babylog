#!/usr/bin/env python3
# -*- coding: utf-8 -*
from setuptools import setup, find_packages
import os


def read(filename):
    return open(filename).read()


def parse_requirements(filename):
    lines = (line.strip() for line in open(filename))
    return [line for line in lines if line and not line.startswith("#")]


BASE_DIR = os.path.dirname(os.path.realpath(__file__))
reqs_filename = os.path.join(BASE_DIR, 'requirements.txt')
readme_filename = os.path.join(BASE_DIR, 'README.md')

setup(
    name="babylog",
    version="0.0.1",
    author="Paweł Należyty",
    author_email="nalezyty.pavel@gmail.com",
    description="A simple Prolog system intended for academic purposes",
    license="Apache License 2.0",
    keywords="prolog",
    install_requires=parse_requirements(reqs_filename),
    url="https://github.com/pawelnalezyty/babylog",
    packages=find_packages(),
    include_package_data=True,
    package_data={'templates': ['*'], 'data': ['*']},
    long_description=read(readme_filename),
    entry_points={
        'console_scripts': ['babylog=babylog.cli:main'],
    },
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3"
    ],
)
