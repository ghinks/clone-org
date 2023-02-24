Clone github namespace
==============================
Clone an organization's repos.
A common situation that folks find themselves in when starting to work with an organization is
the ability to check out all the code and essentially familiarize themselves with the code base
and even grep the code base looking for things.
read_namespace is designed to lessen the pain and give you a one stop clone the organization
toolkit.
This module queries the github graphql endpoint and you must have 'GITHUB_TOKEN' defined in your
environment for the organization to be queried. The clone may be optionally either https or ssh

This is a module that exposes a console script *clone-org* that can clone
all the repositories for the given organization

Installing
==============================
.. code-block:: text

    $ pip install read-github-namespace

A Simple Example
==============================
.. code-block:: text

    $ clone-org -o kubernetes-client -p https -f ~/dev/kub-client-repos

Help
========================================

.. code-block:: text

    $ clone-org -h

.. code-block:: text

    usage: clone-org [-h] -o ORGANIZATION [-p {https,ssh}] [-f FOLDER] [-d]

    Clone an organization's repos. A common situation that folks find themselves in when starting
    to work with an organization is the ability to check out all the code and essentially
    familiarize themselves with the code base and even grep the code base looking for things.
    read_namespace is designed to lessen the pain and give you a one stop clone the organization
    toolkit. This module queries the github graphql endpoint and you must have 'GITHUB_TOKEN'
    defined in your environment for the organization to be queried. The clone may be optionally
    either https or ssh

    options:
      -h, --help            show this help message and exit
      -o ORGANIZATION, --organization ORGANIZATION
                            The organization in Github that you wish to clone all the
                            repositories for.
      -p {https,ssh}, --protocol {https,ssh}
                            The protocol to use either https , which will require GITHUB_TOKEN to
                            be defined in your environment variables. Or ssh which will require
                            that you have your ssh keys set up in current shell.
      -f FOLDER, --folder FOLDER
                            The target folder should be a fully qualified name and the directory
                            structures tested are OSx and Linux. An example would be -f
                            /home/Users/alice/dev/
      -d, --dry-run         The user may simply wish to query the organization before cloning.
                            The dry run option will print out the repositories in the
                            organization specified and exit.