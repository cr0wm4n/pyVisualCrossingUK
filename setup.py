"""Package Setup."""

import setuptools

with open("README.md") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyVisualCrossingUK",
    version="0.1.16.10",
    author="cr0wm4n",
    author_email="crowman4pairs@hotmail.com",
    description="Gets the weather data from Visual Crossing with UK measurements",
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cr0wm4n/pyVisualCrossingUK",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
    ],
)
