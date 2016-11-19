import os
import json
from setuptools import setup, find_packages

GITHUB_URL = 'https://github.com/mistercrunch/airflow-webserver'
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
PACKAGE_DIR = os.path.join(BASE_DIR, 'airflow-webserver', 'assets')
PACKAGE_FILE = os.path.join(PACKAGE_DIR, 'package.json')

with open(PACKAGE_FILE) as f:
    version_string = json.load(f)['version']

setup(
    name='airflow_webserver',
    description=("A web server for the Airflow platform"),
    version=version_string,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    #scripts=['superset/bin/superset'],
    install_requires=[
        'airflow>=1.7.0',
        'flask_appbuilder',
    ],
    tests_require=[
        'nose',
    ],
    author='Maxime Beauchemin',
    author_email='maximebeauchemin@gmail.com',
    url='https://github.com/mistercrunch/airflow-webserver',
    download_url=GITHUB_URL + '/tarball/' + version_string,
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
