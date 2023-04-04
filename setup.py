from setuptools import setup, find_packages

setup(
    name="oslilib", version="0.1",
    description="Open Source License Identification Library",
    author="Andrew Barrier",
    author_email="alkamod@protonmail.com",
    packages=find_packages(),
    install_requires=["scikit-learn", ],
    url='https://oslilib.com',
    package_data={
        '': ['*.txt'],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        ],
)