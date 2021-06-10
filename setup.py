import setuptools
import unittest
import os

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

print(os.getcwd())
def test_pyperplot():
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('./src/pyperplot/tests', pattern='test_*.py')
    return test_suite

setuptools.setup(
    name="pyperplot", # Replace with your own username
    version="0.0.9",
    author="LI Xiaodong",
    author_email="flumer@qq.com",
    description="A package beautifys figures in writing papers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/disadone/pyperplot",
    project_urls={
        "Bug Tracker": "https://github.com/disadone/pyperplot",
    },
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"":"src"},
    package_data={"":["styles/*.mplstyle"]},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
    test_suite='setup.test_pyperplot'
)