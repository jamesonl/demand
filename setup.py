import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="demand",
    version="0.0.0.1",
    author="Jameson Lee",
    author_email="jameson.lee@emergence.studio",
    description="An all encompassing suite for demand forecasting.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jamesonl/demand",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8.2',
)
