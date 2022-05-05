from setuptools import setup

setup(
    version="0.2.1",
    install_requires=[
        "colorama",
    ],
    name="foo_baz",
    package_dir={"foo": ".."},
    packages=[
        "foo.baz",
        "foo.bar",  # dependency
    ],
)
