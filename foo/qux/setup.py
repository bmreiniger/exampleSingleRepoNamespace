from setuptools import setup

setup(
    version="0.2.1",
    install_requires=[
        "us>=1.0.0",
    ],
    name="foo_qux",
    package_dir={"foo": ".."},
    packages=["foo.qux"],
)
