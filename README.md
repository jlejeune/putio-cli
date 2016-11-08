putio-cli
=========

[![Build Status](https://travis-ci.org/jlejeune/putio-cli.svg?branch=master)](https://travis-ci.org/jlejeune/putio-cli)
[![Coverage Status](https://coveralls.io/repos/github/jlejeune/putio-cli/badge.svg?branch=master)](https://coveralls.io/github/jlejeune/putio-cli?branch=master)

*A command line program in Python to talk to Put.io Rest API*


Installation
------------

If you've cloned this project, and want to install the library (*and all
development dependencies*), the command you'll want to run is:

```
pip install -r requirements.txt
```

If you'd like to run all tests for this project, you would run the following
command:

```
pip install -e "putio-cli[test]"
python setup.py test
```

Or just use tox to run them:

```
tox
```

Configuration
-------------

1. You need to register an app in your Put.io account
    Please follow instructions [here](https://put.io/v2/oauth2/register).

    Only name and description fields are required.

    When your app is well registered, oauth token will be generated, you need to keep it in a safe place for future usages.

2. Then, you need to create a putio-cli configuration file using this command:
    ```
    putio-cli config template
    ```

3. Fill your putio-cli configuration file with your dedicated oauth token:
    ```
    cat /Users/jlejeune/.putio-cli/config.ini
    [Settings]
    oauth-token = XXXXXX
    ```
