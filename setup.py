# coding: utf-8
from setuptools import setup, find_packages
import codecs
from os import path
import io
import re

with io.open("nwpc_data_tool/__init__.py", "rt", encoding="utf8") as f:
    version = re.search(r'__version__ = "(.*?)"', f.read()).group(1)

here = path.abspath(path.dirname(__file__))

with codecs.open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='nwpc-data-tool',

    version=version,

    description='A data tool.',
    long_description=long_description,
    long_description_content_type='text/markdown',

    url='https://github.com/perillaroc/nwpc-data-tool',

    author='perillaroc',
    author_email='perillaroc@gmail.com',

    license='GPLv3',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],

    keywords='nwpc data grib2',

    packages=find_packages(exclude=['docs', 'tests', 'example']),

    include_package_data=True,

    install_requires=[
        "pyyaml",
        "jinja2",
        "numpy",
        "pandas",
        "xarray",
        "eccodes-python",
        "dask",
        "click",
        "tqdm",
    ],

    extras_require={
        "cfgrib": [
            "cfgrib",
        ],
        "test": ['pytest'],
        "cov": ['pytest-cov', 'codecov']
    },

    entry_points={
        "console_scripts": [
        ],
    }
)
