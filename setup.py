#!/usr/bin/env python3

from os import path
from setuptools import setup, find_packages

this_directory = path.abspath(path.dirname(__file__))

with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='seo-seoanalyzer',
    version='0.0.1',
    description='An SEO tool that analyzes the structure of a html, and warns of any technical SEO issues based on configured rules',
    author='Sanjaya Bandara',
    author_email='arstbandara@gmail.com',
    url='https://github.com/sanjayatb/seo-analyzer',
    packages=find_packages(),
    keywords=['search engine optimization', 'seo'],
    package_data={'seoanalyzer': ['testFiles/test1.html']},
    include_package_data=True,
    install_requires=[],
    entry_points={
        'console_scripts' : [
            'analyze = seoanalyzer.__main__:main'
        ]
    },
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Topic :: Internet :: WWW/HTTP :: Indexing/Search",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing",
        "Topic :: Internet :: WWW/HTTP",
    ],
    zip_safe=False,
    long_description=long_description,
    long_description_content_type='text/markdown'
)
