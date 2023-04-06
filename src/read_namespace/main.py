from .query_github.fetch_org_repos import collate, \
    fetch_org_repos
from .clone.shell_clone import clone_list, matches_given_language
from .arg_parsing.parse_cmd_line import parse_cmd_line, split_languages
from tabulate import tabulate
from .utils.check_dict import nested_keys_exist


def tabulate_nodes(nodes, url_protocol, languages):
    table = []
    check_list = ["primaryLanguage", "name"]
    for node in nodes:
        if type(node) is dict:
            primary_language = "not defined"
            # get the primary language if given
            if nested_keys_exist(node, check_list) and \
                    node["primaryLanguage"]["name"]:
                primary_language = node["primaryLanguage"]["name"]
            # if no languages given just add all
            if len(languages) == 0:
                table.append([node["name"], node[url_protocol],
                              primary_language])
            # if languages were defined check them
            if len(languages) > 0 and matches_given_language(languages,
                                                             primary_language):
                table.append([node["name"], node[url_protocol],
                              primary_language])
    table_data = tabulate(table, headers=["name", "url", "language"],
                          tablefmt="github")
    print(table_data)
    return table_data


def clone():
    args = parse_cmd_line()
    organization = args["org"]
    url_protocol = args["url_proto"]
    to_folder = args["to_folder"]
    dry_run = args["dry_run"]
    languages = split_languages(args.get("languages"))
    results = fetch_org_repos(organization)
    nodes = collate(results)

    tabulate_nodes(nodes, url_protocol, languages)
    if not dry_run:
        clone_list(nodes, to_folder, url_protocol, languages)


if __name__ == "__main__":
    clone()
