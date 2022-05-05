from setuptools import find_namespace_packages, setup

setup(
    install_requires=[
        "numpy>=1.15.3",
    ],
    name="foo",
    packages=find_namespace_packages(),
    extras_require={
        "dev": ["black", "pytest"],
    }
)
