"""The base command."""

import ConfigParser
import os

import putiopy


class Base(object):
    """A base command."""

    def __init__(self, options):
        self.options = options

    def run(self):
        raise NotImplementedError(
            'You must implement the run() method yourself!')


class BaseClient(Base):
    """A base client command."""

    def __init__(self, options):
        # update options from config file
        config = ConfigParser.RawConfigParser()
        config.read(os.path.expanduser(options['--config']))
        for section in config.sections():
            for key, value in config.items(section):
                key = section + '.' + key
                options[key] = value

        Base.__init__(self, options)

        # define putio client
        self.client = putiopy.Client(options['Settings.oauth-token'])

    def run(self):
        raise NotImplementedError(
            'You must implement the run() method yourself!')
