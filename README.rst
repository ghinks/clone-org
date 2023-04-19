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

usage: clone-org [-h] [-o ORGANIZATION] [-l LANGUAGES] [-p {https,ssh}]
                 [-f FOLDER] [-c] [-d] [-v]

Clone an organization's repos. A common situation that folks find themselves
in when starting to work with an organization is the ability to check out all
the code and essentially familiarize themselves with the code base and even
grep the code base looking for things. read_namespace is designed to lessen
the pain and give you a one stop clone the organization toolkit. This module
queries the github graphql endpoint and you must have 'GITHUB_TOKEN' defined
in your environment for the organization to be queried. The clone may be
optionally either https or ssh

options:
  -h, --help            show this help message and exit
  -o ORGANIZATION, --organization ORGANIZATION
                        The organization in Github that you wish to clone all
                        the repositories for
  -l LANGUAGES, --languages LANGUAGES
                        Github classes languages with well known names such as
                        Python, Go, shell etc. You may pass a filter -l python
                        and it will compare it to the given primary language
                        assigned to the repo. Comma separated strings such as
                        python,java,javascript are also accepted. Names are
                        defined by github in the github/linguist repo.
  -p {https,ssh}, --protocol {https,ssh}
                        The protocol to use either https , which will require
                        GITHUB_TOKEN to be defined in your environment
                        variables. Or ssh which will require that you have
                        your ssh keys set up in current shell.
  -f FOLDER, --folder FOLDER
                        The target folder should be a fully qualified name and
                        the directory structures tested are OSx and Linux. An
                        example would be -f /home/Users/alice/dev/
  -c, --create          To create the target folder set this flag and the
                        directory structure will be created if possible An
                        example would be clone-org -o your_org_name -p https
                        -f ~/temp/my_repos -c
  -d, --dry-run         The user may simply wish to query the organization
                        before cloning. The dry run option will print out the
                        repositories in the organization specified and exit.
  -v, --version         Print version and exit
