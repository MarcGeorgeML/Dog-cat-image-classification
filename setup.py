from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

REPO_NAME = "Dog-vs-Cat-Classifier"
AUTHOR_USER_NAME = "Yoyobun1"
SRC_REPO = "src"
LIST_OF_REQUIREMENTS = ["matplotlib","tensorflow"]

setup(
    name=SRC_REPO,
    version="0.0.1",
    author = "Yoyobun1",
    descritpion = "A simple Classifier to differentiate between Cats and Dogs",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = f"https://github.com/Yoyobun1/Dog-vs-Cat-Classifier",
    author_email = "marcgeorgenow@gmail.com",
    packages = [SRC_REPO],
    python_requires = ">=3.6",
    install_requires = LIST_OF_REQUIREMENTS,
)
