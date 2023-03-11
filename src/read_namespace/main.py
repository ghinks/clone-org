from .query_github.fetch_org_repos import collate, \
    fetch_org_repos
from .shell_cmds.shell_clone import clone_list
from .arg_parsing.parse_cmd_line import parse_cmd_line
from tabulate import tabulate


def tabulate_nodes(nodes, url_protocol):
    table = []
    for node in nodes:
        row = [node["name"], node[url_protocol]]
        table.append(row)
    print(tabulate(table, headers=["name", "url"], tablefmt="github"))


def clone():
    args = parse_cmd_line()
    organization = args["org"]
    url_protocol = args["url_proto"]
    to_folder = args["to_folder"]
    dry_run = args["dry_run"]
    results = fetch_org_repos(organization)
    nodes = collate(results)
    tabulate_nodes(nodes, url_protocol)
    if not dry_run:
        clone_list(nodes, to_folder, url_protocol)


if __name__ == "__main__":
    clone()
