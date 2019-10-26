#!/usr/bin/env python

from distutils.core import setup
from _version import version


def load_requirements(req_file):
    with open(req_file, 'r') as fp:
        packages = fp.read().splitlines()
    return packages

setup(
    name="ipear",
    version=version,
    description="Simple pandas plotly wrapper",
    author="Omer Cinal",
    author_email="omercinal3@gmail.com",
    url="https://github.com/OmerCinal/iplot",
    install_requires=load_requirements('requirements.txt'),
)
