from setuptools import setup, find_packages


VERSION = '0.0.1'
DESCRIPTION = "A python library to query and manage github's dependabot alerts"
LONG_DESCRIPTION = "A python package to query and manage github's dependabot alerts"

# Setting up
setup(
    name="pyDependabot",
    version=VERSION,
    author="Or1337 (Or Elias)",
    author_email="<orelias.tm@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['gql', 'packaging'],
    keywords=['python', 'Dependabot', 'github', 'security', 'open source security'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)