import os
from pathlib import Path
import sgqlc.endpoint.http
from ..utils.check_dict import nested_keys_exist
from math import ceil
from tabulate import tabulate
from ..clone.shell_clone import matches_given_language


# TODO create a unit test ,
# look into [mock](https://pypi.org/project/pytest-asyncio/)
def org_graph_query(organization, query_file, variables):
    """Execute Graph query against GitHub API, using a query and variables"""
    token = os.getenv("GITHUB_TOKEN")
    headers = {
        'Authorization': 'Bearer ' + token
    }
    if not token:
        raise ValueError("No GITHUB_TOKEN in environment variables")
    url = 'https://api.github.com/graphql'
    # Provide a GraphQL query
    query = ""
    query_file = Path(__file__).with_name(query_file)
    with query_file.open('r') as f:
        query = f.read()
    endpoint = sgqlc.endpoint.http.HTTPEndpoint(url, headers)
    result = endpoint(query, variables)

    return result


def fetch_num_org_repos(organization):
    """Fetch the number of repositories in an organization"""
    variables = {
        "login": organization
    }
    return org_graph_query(organization, "org-repos-count.graphql", variables)


def fetch_org_repos(organization, page_sz, after=None):
    """Fetch the repositories in an organization by page size"""
    variables = {
        "login": organization,
        "first": page_sz,
        "after": after
    }
    return org_graph_query(organization, "org-repos.graphql", variables)


def paginate_over_org(organization):
    """Paginate over organizations repositories"""
    page_size = 50
    count_data = fetch_num_org_repos(organization)
    count = 0
    try:
        if nested_keys_exist(count_data,
                             ["data", "organization", "repositories",
                              "totalCount"]):
            count = count_data["data"]["organization"]["repositories"][
                "totalCount"]
    except Exception as err:
        print("Error fetching the count of repos due to the response "
              "count nesting")
        raise err
    pages = ceil(count / page_size) + 1
    after = None
    nodes = []
    for page_count in range(1, pages):
        org_data = fetch_org_repos(organization, page_size, after)
        nodes.extend(collate(org_data))
        if nested_keys_exist(org_data, ["data", "organization", "repositories",
                                        "pageInfo", "endCursor"]):
            page_info = org_data["data"]["organization"]["repositories"][
                "pageInfo"]
            after = page_info["endCursor"]
            has_next_page = page_info["hasNextPage"]
            if not has_next_page:
                break
    return nodes


def tabulate_nodes(nodes, url_protocol):
    table = []
    check_list = ["primaryLanguage", "name"]
    for node in nodes:
        if type(node) is dict:
            # get the primary language if given
            primary_language = get_prim_lang(check_list, node)
            table.append([node["name"], node[url_protocol], primary_language])
    table_data = tabulate(table, headers=["name", "url", "language"],
                          tablefmt="github")
    print(table_data)
    return table_data


def get_prim_lang(check_list, node):
    primary_language = "not defined"
    if nested_keys_exist(node, check_list) and \
            node["primaryLanguage"]["name"]:
        primary_language = node["primaryLanguage"]["name"]
    return primary_language


def filter_by_language(nodes, languages):
    filtered_nodes = []
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
                filtered_nodes.append(node)
            # if languages were defined check them
            if len(languages) > 0 and matches_given_language(languages,
                                                             primary_language):
                filtered_nodes.append(node)
    return filtered_nodes


def collate(query_response):
    try:
        nodes = query_response["data"]["organization"]["repositories"]["nodes"]
        return nodes
    except Exception as err:
        nested_keys_exist(query_response,
                          ["data", "organization", "repositories", "nodes"])
        print(f"Unexpected {err}")
        raise err
