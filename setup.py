from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="processing_image",
    version="0.0.1",
    author="Matheus Caires",
    author_email="caires2100@gmail.com",
    description="README.md",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/matheus-cairesc/proceessing_image.git"
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)