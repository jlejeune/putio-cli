"""Tests for our main putio-cli module."""


from subprocess import PIPE, Popen as popen
from unittest import TestCase

from putio_cli import __version__ as VERSION


class TestHelp(TestCase):
    def test_returns_usage_information(self):
        output = popen(['python', 'putio-cli', '-h'], stdout=PIPE).communicate()[0]
        self.assertTrue('Usage:' in output)

        output = popen(['python', 'putio-cli', '--help'], stdout=PIPE).communicate()[0]
        self.assertTrue('Usage:' in output)


class TestVersion(TestCase):
    def test_returns_version_information(self):
        output = popen(['python', 'putio-cli', '--version'], stdout=PIPE).communicate()[0]
        self.assertEqual(output.strip(), VERSION)
