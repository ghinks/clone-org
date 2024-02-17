import re
import argparse
import os
import importlib.metadata


def parse_cmd_line():
    """parse the command line arguments for the program

    :return:
    Dictionary containing the org and the url type to use
    with GitHub.
    """
    description = """
    Clone an organization's repos.  A common situation that folks find
    themselves in when starting to work with an organization is the ability to
    check out all the code and essentially familiarize themselves with the code
    base and even grep the code base looking for things.  clone_org is
    designed to lessen the pain and give you a one stop clone the organization
    toolkit.  This module queries the github graphql endpoint and you must have
    'GITHUB_TOKEN' defined in your environment for the organization to be
    queried. The clone may be optionally either https or ssh
    """
    parser = argparse.ArgumentParser(description=description)
    org_help = """
    The organization in Github that you wish to clone all the repositories for
    """
    # we cannot make org required as we want the -v option for version
    parser.add_argument('-o', '--organization', required=False, help=org_help)
    language_help = """
    Github classes languages with well known names such as Python, Go, shell
    etc. You may pass a filter -l python and it will compare it to the given
    primary language assigned to the repo. Comma separated strings such as
    python,java,javascript are also accepted. Names are defined by github
    in the github/linguist repo.
    """
    parser.add_argument("-l", "--languages", help=language_help,
                        type=str, default="")
    proto_help = """
    The protocol to use either https , which will require GITHUB_TOKEN to be
    defined in your environment variables. Or ssh which will require that you
    have your ssh keys set up in current shell.
    """
    parser.add_argument('-p', '--protocol', type=str, choices=["https", "ssh"],
                        default="https", help=proto_help)
    to_folder_help = """
    The target folder should be a fully qualified name and the directory
    structures tested are OSx and Linux.  An example would be -f
    /home/Users/alice/dev/
    """
    parser.add_argument("-f", "--folder", type=str, default=os.getcwd(),
                        help=to_folder_help)
    create_folder_help = """
    To create the target folder set this flag and the directory structure will
    be created if possible An example would be clone-org -o your_org_name -p
    https -f ~/temp/my_repos -c
    """
    parser.add_argument("-c", "--create", action="store_true",
                        help=create_folder_help)
    dry_run_help = """
    The user may simply wish to query the organization before cloning. The dry
    run option will print out the repositories in the organization specified
    and exit.
    """
    parser.add_argument("-d", "--dry-run", action="store_true",
                        help=dry_run_help)
    version_help = """
    Print version and exit
    """
    parser.add_argument("-v", "--version", action="store_true",
                        help=version_help)
    args = parser.parse_args()
    url = get_url_type(args)
    if args.dry_run and args.create:
        parser.error("Cannot create a folder in a dry run")
        exit(0)
    if args.version is False and args.organization is None:
        parser.error("The -o organization argument is required")
        exit(0)
    if args.version:
        print_toml_version()
        exit(0)
    elif args.create and not args.dry_run:
        create_new_folder(args.folder)
    elif args.dry_run:
        pass
    else:
        if not check_folder_exists(args.folder):
            raise ValueError(f"Folder {args.folder} does not exist")
    return dict([("org",
                  args.organization),
                 ("url_proto",
                  url),
                 ("to_folder",
                  args.folder),
                 ("dry_run",
                  args.dry_run),
                 ("languages",
                  split_languages(args.languages))])


def check_folder_exists(to_folder):
    return os.path.isdir(to_folder)


def get_url_type(args):
    url = "url"
    if args.protocol == "ssh":
        url = "sshUrl"
    return url


def create_new_folder(to_folder):
    if not check_folder_exists(to_folder):
        print(f"Creating folder {to_folder}")
        os.mkdir(to_folder)


def print_toml_version():
    version = importlib.metadata.version("clone-org")
    print(f"Current version is {version}")


def split_languages(languages):
    """parse languages for a list option and return a list of languages"""
    if re.search(".*,{1,}.*", languages):
        return languages.split(",")
    # no comma separated lists
    elif len(languages) > 0:
        return [languages]
    # empty array is falsy whereas a split on an empty array produces a
    # non-empty array
    return []
