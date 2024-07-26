# Responsible for distributing this project as a Python Project

import os
from setuptools import setup, find_packages
from typing import List

# -e. maps the requirements file to setup file
HYPHEN_E_DOT = '-e .'

# This function reads requirements.txt file content

def read(file_name:str) -> List[str]:
    requirements = []

    with open(file_name) as file_obj:
        requirements = file_obj.readlines()
        requirements= [req.replace('\n', ' ') for req in requirements]

    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)

    return requirements


# Metadata for project
setup(
    name = "ML End-to-End Project",
    version = "0.0.1",
    author = "Ayyam",
    author_email = "anishgauri00786@gmail.com",
    license = "BSD",
    packages= find_packages(),
    install_requires = read('requirements.txt')
)