from .query_github.fetch_org_repos import fetch_repo_by_page, tabulate_nodes
from .clone.shell_clone import clone_list
from .arg_parsing.parse_cmd_line import parse_cmd_line


def clone():
    args = parse_cmd_line()
    org = args["org"]
    url_proto = args["url_proto"]
    to_folder = args["to_folder"]
    dry_run = args["dry_run"]
    languages = args.get("languages")
    nodes = fetch_repo_by_page(org)
    tabulate_nodes(nodes, url_proto, languages)
    if not dry_run:
        clone_list(nodes, to_folder, url_proto, languages)


if __name__ == "__main__":
    clone()
