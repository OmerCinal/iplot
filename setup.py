#!/usr/bin/env python

from distutils.core import setup

import sys
from ._version import version

sys.path.append("/iplot")

setup(
    name="ipear",
    version=version,
    description="Simple pandas plotly wrapper",
    author="Omer Cinal",
    author_email="omercinal3@gmail.com",
    url="https://github.com/OmerCinal/iplot",
    packages=["plotly", "pandas", "distutils", "distutils.command"],
)
