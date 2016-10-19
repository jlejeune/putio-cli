"""The base command."""

import putio

class Base(object):
    """A base command."""

    def __init__(self, options):
        self.options = options

        # define putio client
        self.client = putio.Client(options['--oauth_token'])

    def run(self):
        raise NotImplementedError('You must implement the run() method yourself!')
