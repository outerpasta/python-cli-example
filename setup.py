"""setup.py"""
from setuptools import setup, find_packages

setup(
    name='example',
    version='0.0.1',
    description='Example of an awesome python cli project',
    packages=find_packages(),
    include_package_data=True,
    install_requires='''
    argh
    argparse
    ''',
    entry_points={
        'console_scripts': [
            'example=example.__main__:main'
        ],
    }
)
