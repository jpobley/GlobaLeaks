#!/usr/bin/env python
#-*- coding: utf-8 -*-
from __future__ import print_function

from importlib import import_module
import sys

import pip
from setuptools import find_packages, setup
from setuptools.command.test import test as _TestCommand

import globaleaks

install_requires = [str(r.req) for r in pip.req.parse_requirements('requirements.txt',
                                                                   session=pip.download.PipSession())]


class TestCommand(_TestCommand):
    def run_tests(self):
        from twisted.trial import runner, reporter

        testsuite_runner= runner.TrialRunner(reporter.TreeReporter)
        loader = runner.TestLoader()
        suite = loader.loadPackage(import_module(self.test_suite), True)
        test_result = testsuite_runner.run(suite)
        sys.exit(not test_result.wasSuccessful())

setup(
    name='globaleaks',
    version=globaleaks.__version__,
    author=globaleaks.__author__,
    author_email=globaleaks.__email__,
    license=globaleaks.__license__,
    url='https://globaleaks.org/',
    cmdclass={'test': TestCommand},
    package_dir={'globaleaks': 'globaleaks'},
    test_suite='globaleaks.tests',
    package_data={'globaleaks': [
        'db/sqlite.sql',
    ]},
    packages=find_packages(exclude=['*.tests', '*.tests.*']),
    scripts=[
        'bin/globaleaks',
        'bin/gl-admin',
        'bin/gl-fix-permissions',
    ],
    install_requires=install_requires
)
