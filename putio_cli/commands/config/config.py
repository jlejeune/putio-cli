"""The config command."""

import os

from putio_cli.commands.base import Base


class Config(Base):
    """
    config command to manage configuration file

    Usage:
      putio-cli config <command>

    Commands:
      template                 write a template configuration file in ~/.putio-cli/config.ini
      show                     show config file
    """

    def __init__(self, options):
        Base.__init__(self, options)
        self.cfgfilename = os.path.expanduser(self.options['--config'])

        # create dir if needed
        cfgfiledir = os.path.dirname(self.cfgfilename)
        if not os.path.exists(cfgfiledir):
            os.mkdir(cfgfiledir)

    def run(self):
        raise NotImplementedError(
            'You must implement the run() method yourself!')
