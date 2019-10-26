#!/usr/bin/env python

from distutils.core import setup
from ipear._version import version

setup(
    name="ipear",
    version=version,
    description="Simple pandas plotly wrapper",
    author="Omer Cinal",
    author_email="omercinal3@gmail.com",
    url="https://github.com/OmerCinal/iplot",
    install_requires=[
        'plotly',
        'pandas',
    ]
)
