import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="organize-me",
    version="1.0.0",
    author="zackbunch",
    author_email="zackbunch96@gmail.com",
    description="A simple file organizer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zackbunch/Organize-Me",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
