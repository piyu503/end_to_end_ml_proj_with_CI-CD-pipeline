from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    This function returns list of requirements
    '''
    Hyphen="-e ."
    

    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
    if Hyphen in requirements:
        requirements.remove(Hyphen)

setup(
    name="mlproject",
    version="0.001",
    author="Piyush",
    author_email="piyush.8548@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)