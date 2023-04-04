from setuptools import setup, find_packages

setup(
    name='license-identifier',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'scikit-learn',
    ],
    package_data={
        '': ['*.txt'],
    },
)