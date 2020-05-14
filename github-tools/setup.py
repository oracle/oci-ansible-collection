import io
import os
from setuptools import setup, find_packages
here = os.path.abspath(os.path.dirname(__file__))

with io.open((os.path.join(here, "requirements.txt")), "r") as f:
    requires = [line.strip() for line in f.readlines()]

setup(
    name="github",
    version="1.0",
    entry_points={
        "console_scripts": [
            "github = github.main:cli"
        ]
    },
    description="Oracle Bare Metal Cloud Github Tools",
    author="Oracle",
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    install_requires=requires,
)
