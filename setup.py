#!/usr/bin/env python

import re
from setuptools import find_packages, setup

requires = [
    "phpserialize>=1.3",
]

version = ""
with open("wpparser/__init__.py", "r") as fd:
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', fd.read(), re.MULTILINE
    ).group(1)

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="wpparser",
    version=version,
    description="Parse wordpress export files into a well formatted python dictionary",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Martin Sandström",
    author_email="martin@marteinn.se",
    url="https://github.com/marteinn/wpparser",
    packages=find_packages(),
    package_data={"": ["LICENSE"], "wpparser": ["*.txt"]},
    package_dir={"wpparser": "wpparser"},
    include_package_data=True,
    install_requires=requires,
    license="MIT",
    zip_safe=False,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
