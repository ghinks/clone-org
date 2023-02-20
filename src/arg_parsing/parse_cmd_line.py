import argparse
import os


def parse_cmd_line():
    """parse the command line arguments for the program

    :return:
    Dictionary containing the org and the url type to use
    with Github.
    """
    description = """
    Clone an organization's repos. 
    A common situation that folks find themselves in when starting to work with an organization is
    the ability to check out all the code and essentially familiarize themselves with the code base
    and even grep the code base looking for things.
    read_github_namespace is designed to lessen the pain and give you a one stop clone the organization
    toolkit.
    """
    parser = argparse.ArgumentParser(description=description)
    org_help = """
    The organization in Github that you wish to clone all the repositories for.
    """
    parser.add_argument('-o', '--organization', required=True, help=org_help)
    proto_help = """
    The protocol to use either https , which will require GITHUB_TOKEN to be defined
    in your environment variables. Or ssh which will require that you have your ssh
    keys set up in current shell.
    """
    parser.add_argument('-p', '--protocol', type=str, choices=["https", "ssh"], default="https", help=proto_help)
    to_folder_help = """
    The target folder should be a fully qualified name and the directory structures tested are OSx and Linux.
    An example would be -f /home/Users/alice/dev/
    """
    parser.add_argument("-f", "--folder", type=str, default=os.getcwd(), help=to_folder_help)
    args = parser.parse_args()
    url = get_url_type(args)
    if not check_folder_exists(args.folder):
        raise ValueError(f"Folder {args.folder} does not exist")
    return dict([("org", args.organization), ("url_proto", url), ("to_folder", args.folder)])

def check_folder_exists(to_folder):
    return os.path.isdir(to_folder)

def get_url_type(args):
    url = "url"
    if args.protocol == "ssh":
        url = "sshUrl"
    return url
