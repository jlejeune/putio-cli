"""Packaging settings."""


from codecs import open
from os.path import abspath, dirname, join

from setuptools import find_packages, setup
from setuptools.command.test import test as TestCommand

from putio_cli import __version__


this_dir = abspath(dirname(__file__))
with open(join(this_dir, 'README.md'), encoding='utf-8') as file:
    long_description = file.read()


class Tox(TestCommand):
    """Run all tests."""
    description = 'run tests'
    user_options = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import tox
        import sys
        errcode = tox.cmdline(self.test_args)
        sys.exit(errcode)

setup(
    name='putio-cli',
    version=__version__,
    description='A command line program in Python to talk to Put.io Rest API',
    long_description=long_description,
    url='https://github.com/jlejeune/putio-cli',
    author='Julien LE JEUNE',
    author_email='mail.julien.le.jeune@gmail.com',
    license='MIT',
    classifiers=[
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='putio-cli',
    packages=find_packages(exclude=['docs', 'tests*']),
    install_requires=['docopt', 'putio.py'],
    extras_require={
        'test': ['tox', 'nose', 'coverage'],
    },
    tests_require=['tox'],
    scripts=['putio-cli'],
    cmdclass={'test': Tox},
)
