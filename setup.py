from setuptools import setup, find_packages

setup(
    name="oslili", version="0.3",
    description="Open Source License Identification Library",
    author="Oscar Valenzuela",
    author_email="oscar.valenzuela.b@gmail.com",
    packages=['oslili', 'oslili.spdx'],
    install_requires=["scikit-learn", ],
    url='https://opensourcelicensecompliance.com',
    package_data={
        "oslili.spdx": ["*.txt",],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        ],
)
