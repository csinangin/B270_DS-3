from setuptools import setup, find_packages

setup(
    name="B270_DS-3",
    version="0.1",
    packages=find_packages(),
    description="A package for Machine Learning Toolkit",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/csinangin/B270_DS-3",
    author="Cenk SİNANGİN",
    author_email="cenk.sinangin@gmail.com",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)