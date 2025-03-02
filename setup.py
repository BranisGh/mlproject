from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Krish',
    author_email='krishnaik06@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)













# import setuptools
# from typing import List

# def get_readme(file_path: str) -> str:
#     """
#     Reads the contents of a file and returns it as a string.
    
#     Args:
#         file_path (str): The path to the file to be read.

#     Returns:
#         str: The content of the file as a string.
#     """
#     with open(file_path, "r", encoding="utf-8") as f:
#         long_description = f.read()
#     return long_description

# HYPEN_E_DOT = '-e .'

# def get_requirements(file_path: str) -> List[str]:
#     """
#     Reads a requirements file and returns a list of requirements.

#     Args:
#         file_path (str): The path to the requirements file.

#     Returns:
#         List[str]: A list of requirements as strings.
#     """
#     requirements = []
#     with open(file_path) as file_obj:
#         requirements = file_obj.readlines()
#         requirements = [req.strip() for req in requirements]

#         if HYPEN_E_DOT in requirements:
#             requirements.remove(HYPEN_E_DOT)

#     return requirements

# __version__ = "0.0.0"  # Package version

# REPO_NAME = "mlproject"
# AUTHOR_USER_NAME = "BranisGh"
# SRC_REPO = "mlops standard project"
# AUTHOR_EMAIL = "branisghoul02@hotmail.com"

# def setup_package():
#     """
#     Configures and sets up the Python package using setuptools.
#     """
#     setuptools.setup(
#         name=REPO_NAME,
#         version=__version__,
#         author=AUTHOR_USER_NAME,
#         author_email=AUTHOR_EMAIL,
#         description=SRC_REPO,
#         long_description=get_readme("README.md"),
#         long_description_content_type="text/markdown",
#         url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
#         project_urls={
#             "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
#         },
#         packages=setuptools.find_packages(where="src"),
#         install_requires=get_requirements('requirements.txt')
#     )

# if __name__ == "__main__":
#     setup_package()
