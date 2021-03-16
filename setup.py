from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name="merpy",
    version="1.7.1",
    description="use MER inside python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Sijia Hao",
    author_email="sijia.hao@ad.unsw.edu.au",
    packages=["merpy"],
    keywords=["ner", "mer"],
    url="https://github.com/a-group-for-seng3011/merpy",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_data={"merpy": ["MER/*", "MER/data/*"]},
    install_requires=["requests"],
    extras_require={"dev": ["setuptools-changelog"]},
)
