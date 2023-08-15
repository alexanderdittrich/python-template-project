from setuptools import find_packages, setup

VERSION = "0.1"
DESCRIPTION = "Bio-inspired learning algorithms"
LONG_DESCRIPTION = "Bio-inspired learning algorithms"

setup(
    name="bioinspired_learning",
    version=VERSION,
    author="Alexander Dittrich",
    author_email="alexander.dittrich@epfl.ch",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    license="MIT License",
    url="https://www.epfl.ch/labs/lis/",
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
)
