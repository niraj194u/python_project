from setuptools import setup, find_packages

setup(
    name='calculator_package',
    version='1.0.0',
    description='A simple calculator package',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'calculator=calculator.main:main',
        ],
    },
)
