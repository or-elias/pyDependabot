from setuptools import setup, find_packages


DESCRIPTION = "A python library to query and manage github's dependabot alerts"


# Setting up
setup(
    name="pydependabot",
    version='0.8',
    author="Or1337 (Or Elias)",
    author_email="<orelias.tm@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=open("README.md").read(),
    packages=find_packages(),
    install_requires=['gql', 'packaging'],
    keywords=['python', 'Dependabot', 'github', 'security', 'open source security', "pyDependabot", "pydependabot", "py-dependabot"],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)