#!/usr/bin/env python
"""playground-plugin extension builder and installer."""

import setuptools


name = 'playground-plugin'
desc = """Extension for chaoshub that provides tools for playground"""
author = 'Leonid Haimov'
author_email = 'leonidh@wix.com'

setup_params = dict(
    name=name,
    description=desc,
    version='0.1.0',
    author=author,
    author_email=author_email,
    packages=setuptools.find_packages(),
    include_package_data=True,
    use_scm_version=True,
)


def main():
    """Package installation entry point."""
    setuptools.find_packages()
    setuptools.setup(**setup_params)


if __name__ == '__main__':
    main()
