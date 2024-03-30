from setuptools import find_packages, setup


with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as req:
    requirements = req.readlines()


setup(
    name="crhc-cli",
    version="1.16.16",
    author="Waldirio",
    author_email="waldirio@gmail.com",
    description="This project contains the crhc command line tool that simplifies the use of the C.RH.C API available at console.redhat.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=requirements,
    url="https://github.com/C-RH-C/crhc-cli/",
    packages=find_packages(),
    python_requires=">=3.9",
    scripts=['bin/crhc-cli'],
    include_package_data=True,
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
