# exampleSingleRepoNamespace
a demo for a python namespace package living in a single repository

Most namespace examples assume each subpackage lives in its own directory.
If you already have a large package in one repo but would like to be able to install submodules,
you can break it into a namespace as done here.

Here `foo.baz` depends on `foo.bar`.  
N.B. pip doesn't install transitive dependencies, so if you want to pip-install `foo.baz`,
you should _also explicitly_ install `foo.bar` to pull in the dependency `requests`.
