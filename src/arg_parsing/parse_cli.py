import argparse


def parse_github():
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
    parser.add_argument('-o', '--org', required=True, help=org_help)
    proto_help = """
    The protocol to use either https , which will require GITHUB_TOKEN to be defined
    in your environment variables. Or ssh which will require that you have your ssh
    keys set up in current shell.
    """
    parser.add_argument('-p', '--prot', type=str, choices=["https", "ssh"], default="https", help=proto_help)
    args = parser.parse_args()
    print(args)
    url = get_url_type(args)
    return dict([("org", args.org), ("url", url)])


def get_url_type(args):
    url = "url"
    if args["prot"] == "ssh":
        url = "sshUrl"
    return url
