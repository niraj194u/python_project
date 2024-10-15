from setuptools import setup, find_packages

setup(
    name='student_details',
    version='1.0.0',
    description='A package for managing student details',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'student-details=student_details.main:main',
        ],
    },
)
