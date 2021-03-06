"""Provider for Faker which adds fake names for the AWS ecosystem."""

import setuptools

try:
    with open("README.markdown", "r") as fh:
        long_description = fh.read()  # pylint: disable=invalid-name
except FileNotFoundError:
    # pylint: disable=invalid-name
    long_description = (
        "Provider for [Faker](https://faker.readthedocs.io/) which adds fake "
        "names for the AWS ecosystem."
    )

setuptools.setup(
    name="faker-aws",
    version="1.0.0",
    author="Ditesh Gathani",
    author_email="ditesh@gathani.org",
    description="Provider for Faker which adds fake names for the AWS ecosystem.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ditesh/faker-aws",
    packages=setuptools.find_packages(),
    install_requires=["faker"],
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
