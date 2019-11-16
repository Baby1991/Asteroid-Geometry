import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Asteroid-Geometry-Baby1991",
    version="0.0.2",
    author="Baby1991",
    author_email="dancingbaby1991@gmail.com",
    description="A small Geometry package for Working With Asteroid Shine Simulations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Baby1991/Asteroid-Geometry",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)