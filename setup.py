# This file is use for converting folders into a packages

from setuptools import find_packages,setup
from typing import List

"""
This file is used when we have to deploy this project as 
library. Packaging is must in that case.

find_packages => returns the folders where __init__.py file is located
                 or it will use those folders as packages
"""

HYPEN_E_DOT = '-e .'
# hypen_e_dot is not library to install it is just use for creating packages

                                   # this is return arrow
def get_requirements(filepath :str)-> List[str]:
    requirements = []
    with open(filepath) as file_obj:
        requirements = file_obj.readlines()
        # readlines funtion return \n after every new line so we have remove it
        requirements = [req.replace('\n', '') for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements



setup(
    name='Housing',
    version='0.0.1',
    author= 'Abhishek Wankhade',
    author_email= 'abhishekwankhade4670@gmail.com',
    install_requires = get_requirements('requirements.txt'),
    packages= find_packages()

)