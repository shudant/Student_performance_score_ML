from setuptools import find_packages,setup
from typing import List 


hypen_e_dot ='-e .'
def get_requirement(file_path:str)->List[str]:
    '''
    this function will return the list of requirment
    '''
    requirement=[]
    with open (file_path) as file_obj:
        requirement = file_obj.readlines()
        requirement=[req.replace("\n","") for req in requirement]

        if hypen_e_dot in requirement:
            requirement.remove(hypen_e_dot)
             
    return requirement



setup(
    name = 'Student_performance_score_ML',
    version='0.0.1',
    author='Suddhant',
    author_email='shudantgoutam980a@gmail.com',
    packages=find_packages(),
    install_requires=get_requirement('Requirement.txt')
)