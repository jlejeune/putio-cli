"""The config command."""

import ConfigParser
import os
import sys

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
        subcommand = self.options['<command>']
        if subcommand == 'template':
            if os.path.exists(self.cfgfilename) and os.path.getsize(self.cfgfilename) > 0:
                sys.exit('Config file already exists, please fill it or delete it before launching this subcommand')

            # create a template configuration file
            cfgfile = open(self.cfgfilename, 'w')
            config = ConfigParser.ConfigParser()
            config.add_section('Settings')
            config.set('Settings', 'oauth-token', 'TO REPLACE')
            config.write(cfgfile)
            cfgfile.close()

        elif subcommand == 'show':
            try:
                cfgfile = open(self.cfgfilename, 'r')
            except IOError:
                sys.exit('Config file does not exist, please use template subcommand first')
            print cfgfile.read()
            cfgfile.close()
        else:
            sys.exit("This subcommand '%s' doesn't exist, try `putio-cli config --help`" % subcommand)
