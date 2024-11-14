# setup.py
from setuptools import setup, find_packages

setup(
    name="merge_dataframes",
    version="0.1.0",
    description="A Python package to merge two Pandas DataFrames",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="laxman kusuma",
    author_email="laxman.kusuma@gmail.com",
    url="https://github.com/yourusername/merge_dataframes",
    packages=find_packages(),
    install_requires=[
        "pandas>=1.0.0"
    ],
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
