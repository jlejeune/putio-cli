"""Tests for our `putio-cli config` subcommand."""


from subprocess import PIPE, STDOUT, Popen as popen
from unittest import TestCase
import os


class TestConfig(TestCase):
    test_config_file = '/tmp/putio-cli.ini'

    def test_returns_help(self):
        output = popen(['python', 'putio-cli', 'config', '--help'], stdout=PIPE).communicate()[0]
        self.assertTrue('Usage:' in output)

    def test_create_template(self):
        output = popen(['python', 'putio-cli', '--config', self.test_config_file, 'config', 'template'],
                       stdout=PIPE).communicate()[0]
        self.assertTrue(os.path.exists(self.test_config_file))

        output = popen(['python', 'putio-cli', '--config', self.test_config_file, 'config', 'template'],
                       stdout=PIPE, stderr=STDOUT).communicate()[0]
        self.assertEqual(output.strip(),
                         'Config file already exists, please fill it or delete it before launching this subcommand')

    def test_show_config(self):
        output = popen(['python', 'putio-cli', '--config', self.test_config_file, 'config', 'show'],
                       stdout=PIPE).communicate()[0]
        self.assertEqual(output.replace('\n', '').strip(), '[Settings]oauth-token = TO REPLACE')

        # clean
        os.remove(self.test_config_file)

        output = popen(['python', 'putio-cli', '--config', self.test_config_file, 'config', 'show'],
                       stdout=PIPE, stderr=STDOUT).communicate()[0]
        self.assertEqual(output.strip(),
                         'Config file does not exist, please use template subcommand first')
