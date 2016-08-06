#!/usr/bin/env python3

from setuptools import setup
from setuptools import find_packages
import linky as l

setup(
    name="LinkY",
    description=l.__DESC__,
    long_description=open("README.md").read(),

    version=l.__VERSION__,
    license=l.__LICENSE__,

    url="https://github.com/apizzimenti/LinkY.git",
    author=l.__AUTHOR__,
    author_email=l.__EMAIL__,

    packages=find_packages(),

    entry_points={
        "console_scripts": ["linky=linky.index:main"]
    }
)