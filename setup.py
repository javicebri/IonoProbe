import pathlib
from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent

VERSION = '1.0.0'
PACKAGE_NAME = 'ionoprobe'
AUTHOR = 'Javier Cebrián'
AUTHOR_EMAIL = 'None'
URL = 'https://github.com/javicebri/IonoProbe/'

LICENSE = 'Mit 3'
DESCRIPTION = 'Ionospheric study tools'

INSTALL_REQUIRES = []

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    install_requires=INSTALL_REQUIRES,
    license=LICENSE,
    packages=find_packages(),
    include_package_data=True
)