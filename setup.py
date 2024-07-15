from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT="-e ."
def get_requirements(file_path:str)->List[str]:
    '''This function will return the list of requirements'''
    requirement=[]
    with open(file_path) as file:
        requirement=file.readline()
        requirement=[req.replace("\n","")for req in requirement]

        if HYPEN_E_DOT in requirement:
            requirement.remove(HYPEN_E_DOT)

setup(
    name="mlproject",
    version='0.0.1',
    author='Neelakandan',
    author_email='neelakandan2001@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)