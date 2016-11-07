"""The config template command."""

import ConfigParser
import os
import sys

from putio_cli.commands.config import Config


class Template(Config):
    """
    template command to write a configuration file from template

    Usage:
      putio-cli config template
    """

    def run(self):
        if os.path.exists(self.cfgfilename) and os.path.getsize(self.cfgfilename) > 0:
            sys.exit(
                'Config file already exists, please fill it or delete it before launching this subcommand')

        # create a template configuration file
        cfgfile = open(self.cfgfilename, 'w')
        config = ConfigParser.ConfigParser()
        config.add_section('Settings')
        config.set('Settings', 'oauth-token', 'TO REPLACE')
        config.write(cfgfile)
        cfgfile.close()
