from .query_github.fetch_org_repos import paginate_over_org, tabulate_nodes, \
    filter_by_language
from .clone.shell_clone import clone_list
from .arg_parsing.parse_cmd_line import parse_cmd_line


def clone():
    args = parse_cmd_line()
    org = args["org"]
    url_proto = args["url_proto"]
    to_folder = args["to_folder"]
    dry_run = args["dry_run"]
    languages = args.get("languages")
    nodes = paginate_over_org(org)
    filtered_nodes = filter_by_language(nodes, languages)
    tabulate_nodes(filtered_nodes, url_proto)
    if not dry_run:
        clone_list(filtered_nodes, to_folder, url_proto)


if __name__ == "__main__":
    clone()
