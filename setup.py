#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages


with open("README.md") as readme_file:
    readme = readme_file.read()


requirements = ['cython','requests','beautifulsoup4','PyYaml','lxml','grequests','gevent','twint']


setup(
    author="sham00n",
    author_email="sham00n@protonmail.com",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Environment :: Console",
    ],
    description='Buster is an OSINT tool used to generate and verify emails and return information associated with them',
    install_requires=requirements,
    license="GNU GPLv3 ",
    long_description_content_type='text/markdown',
    long_description=readme + "\n\n",
    include_package_data=True,
    keywords="buster",
    name="buster",
    packages=find_packages(),
    entry_points={"console_scripts": ["buster = buster.__main__:start"]},
    setup_requires=requirements,
    url="https://github.com/sham00n/buster",
    version="1.0.0",
    zip_safe=False,
    package_data={'data': ['email-providers.json','api-keys.yaml','domain_list.json']},
)
