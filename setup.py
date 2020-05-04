"""
setup.py
The setup file containing package metadata, entrypoint directions and package installation requirements.
This file shouldn't be directly interacted with by a user, but instead be activated through a package manager like pip.
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from os import path

base = path.abspath(path.dirname(__file__))
with open(path.join(base, 'README.md'), encoding='utf-8') as f:
    readme = f.read()

setup(
    name='tumble',  # Required
    version='0.0.1',  # Required
    description='A CLI-based Tumblr media scraper',
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/Xevion/tumble',
    author='Xevion',
    author_email='xevion@xevion.dev',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: GNU General Public License',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='tumblr scraper media downloading downloader scraping cli commandline',
    package_dir={'': 'tumble'},
    packages=find_packages(where='tumble'),  # Required
    python_requires='>3.5, <4',
    install_requires=['docopt'],
    extras_require={
    },
    entry_points={
        'tumble': [
            'tumble=tumble.cli:main',
        ],
    },
    project_urls={
        'Bug Reports': 'https://github.com/Xevion/tumble/issues',
        'Source': 'https://github.com/Xevionn/tumble/',
    },
)