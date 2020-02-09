import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="svarlr", 
    version="0.0.1",
    author="Kyle Murphy",
    author_email="kyleevanmurphy@gmail.com",
    description="A package to estimate structural vector autoregression models with a long-run restriction",
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=["svarlr"],
    package_dir={'': 'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
