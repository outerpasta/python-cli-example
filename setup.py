"""setup.py"""
from setuptools import setup, find_packages

setup(
    name='example',
    version='0.0.1',
    description='Example of an awesome python cli project',
    packages=find_packages(),
    # include_package_data=True,
    package_data={
        'example': [
            'resources/*.yml',
            'resources/*.txt',
            'resources/*.csv',
            'resources/.gitkeep'
        ],
    },

    install_requires='''
    argh
    argcomplete
    argparse
    tabulate
    ''',
    extras_require={
        'dev': '''
        ipython
        pytest
        pylint
        tox
    '''},
    entry_points={
        'console_scripts': [
            'example=example.__main__:main'
        ],
    }
)
