from setuptools import find_packages, setup
from typing import List

hyphen_e_dot = "-e ."
def get_requirements(filename: str) -> List[str]:
    '''
    This function reads the requirements.txt file and returns a list of requirements.
    '''
    requirements = []
    with open(filename) as f:
        requirements = f.readlines()
        requirements = [r.replace("\n","") for r in requirements]

        if hyphen_e_dot in requirements:
            requirements.remove(hyphen_e_dot)
        
    return requirements

setup(
    name='myproject',
    version='0.0.1',
    author='Khan',
    author_email='wkhan.ee@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)