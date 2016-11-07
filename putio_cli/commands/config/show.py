"""The config show command."""

import sys

from putio_cli.commands.config import Config


class Show(Config):
    """
    show command to print configuration file

    Usage:
      putio-cli config show
    """

    def run(self):
        try:
            cfgfile = open(self.cfgfilename, 'r')
        except IOError:
            sys.exit(
                'Config file does not exist, please use template subcommand first')
        print cfgfile.read()
        cfgfile.close()
