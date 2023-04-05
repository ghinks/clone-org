from .query_github.fetch_org_repos import fetch_repo_by_page
from .clone.shell_clone import clone_list
from .arg_parsing.parse_cmd_line import parse_cmd_line
from tabulate import tabulate
from .utils.check_dict import nested_keys_exist


def tabulate_nodes(nodes, url_protocol):
    table = []
    check_list = ["primaryLanguage", "name"]
    for node in nodes:
        if type(node) is dict:
            primary_language = "not defined"
            if nested_keys_exist(node, check_list) and \
                    node["primaryLanguage"]["name"]:
                primary_language = node["primaryLanguage"]["name"]
            table.append([node["name"], node[url_protocol], primary_language])
    print(tabulate(table, headers=["name", "url", "language"],
                   tablefmt="github"))


def clone():
    args = parse_cmd_line()
    organization = args["org"]
    url_protocol = args["url_proto"]
    to_folder = args["to_folder"]
    dry_run = args["dry_run"]
    language = args.get("language")
    nodes = fetch_repo_by_page(organization)
    tabulate_nodes(nodes, url_protocol)
    if not dry_run:
        clone_list(nodes, to_folder, url_protocol, language)


if __name__ == "__main__":
    clone()
