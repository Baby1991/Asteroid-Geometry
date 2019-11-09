import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Geometry-Baby1991", # Replace with your own username
    version="0.0.1",
    author="Baby1991",
    author_email="dancingbaby1991@gmail.com",
    description="A small Geometry package",
    long_description=long_description,
    long_description_content_type="geometry",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)