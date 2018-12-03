import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rename_guru",
    version="0.0.7",
    author="sitnarf",
    author_email="sitnarf@gmail.com",
    description="Tool for duplicating code while substituting specified string inside the folder, respecting camelCase, UPPER_CASE etc.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sitnarf/rename-guru",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)