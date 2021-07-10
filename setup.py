from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = []

setup(
    name="stellar",
    version="0.0.3",
    author="Sharad Mishra",
    author_email="imsharadmishra@gmail.com",
    description="A package to merge small files using apache arrow",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/imsharadmishra/homepage/",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.8"
    ],
)