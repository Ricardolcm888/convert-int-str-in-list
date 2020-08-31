import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name="int_str_converter",
    version="0.0.1",
    author="Ricardolcm",
    description="A package that converts all things in a list into either string or int",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        
    ]
)