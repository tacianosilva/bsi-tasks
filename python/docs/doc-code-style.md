# Definições da Formatação do Código do Projeto

## Instalação do flake8

[Flake8](https://pypi.org/project/flake8/) is a wrapper around these tools: PyFlakes, pycodestyle, Ned Batchelder’s McCabe script.

To install it: `pip install flake8`.

Usage: `flake8 {source_file_or_directory}`.

To get statics also `flake8 {source_file_or_directory} --statistics`.

**Flake8** runs all the tools by launching the single flake8 command. It displays the warnings in a per-file, merged output.

* [Flake8 - Full Listing of Options](https://flake8.pycqa.org/en/latest/user/options.html)
* [Flake8 - Error Codes](https://flake8.pycqa.org/en/latest/user/error-codes.html)
* [PyCodeStyle - Error Codes](https://pycodestyle.pycqa.org/en/latest/intro.html#error-codes)
* [PyDocStyle - Error Codes](http://www.pydocstyle.org/en/stable/error_codes.html)

**Flake8** is excellent for expandability. Next we talk about **hacking** which has project own rule in flake8.

### What is hacking

[hacking](https://pypi.org/project/hacking/) is flake8 plug-in which is made based on OpenStack OpenStack Style Guidlines.

To install it: `pip install hacking`.

### Whats is flake8-docstrings

[flake8-docstrings](https://pypi.org/project/flake8-docstrings/) is a simple module that adds an extension for the fantastic [pydocstyle](https://github.com/pycqa/pydocstyle) tool to [flake8](https://gitlab.com/pycqa/flake8).

To install it: `pip install flake8-docstrings`

### Links consultados

* https://siderlabs.com/blog/about-style-guide-of-python-and-linter-tool-pep8-pyflakes-flake8-haking-pyling-7fdbe163079d/
* https://books.agiliq.com/projects/essential-python-tools/en/latest/linters.html#flake8
* https://pypi.org/project/flake8/
* https://github.com/openstack/hacking
