from setuptools import setup

setup(
    version="0.1.0",
    install_requires=[
        "requests>=2.22.0",
    ],
    name="foo_bar",
    package_dir={"foo": ".."},
    packages=["foo.bar"],
)
