from setuptools import setup, find_packages


REQUIRED = [
    "numpy",
    "pandas"
]

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

setup(
    name="lambdata-dspt10-jjb",
    version="0.0.1",  # Version MUST be higher each push
    author="JamesBarciz",
    author_email="jamesjbarciz@gmail.com",
    description="Basic package with helper functions",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/JamesBarciz/lambdata-dspt10-jjb",
    packages=find_packages(),
    install_requires=REQUIRED,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]
)
