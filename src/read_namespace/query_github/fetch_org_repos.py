import os
from pathlib import Path
from sgqlc.endpoint.http import HTTPEndpoint
from ..utils.check_dict import nested_keys_exist
from math import ceil

# TODO create a unit test ,
# look into [mock](https://pypi.org/project/pytest-asyncio/)
def org_graph_query(organization, query_file, variables):
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
    endpoint = HTTPEndpoint(url, headers)
    result = endpoint(query, variables)

    return result


def fetch_num_org_repos(organization):
    variables = {
        "login": organization
    }
    return org_graph_query(organization, "org-repos-count.graphql", variables)


def fetch_org_repos(organization, page_sz, after=None):
    variables = {
        "login": organization,
        "first": page_sz,
        "after": after
    }
    return org_graph_query(organization, "org-repos.graphql", variables)


def fetch_repo_by_page(organization):
    page_size = 50
    count_data = fetch_num_org_repos(organization)
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
    pages = ceil(count/page_size) + 1
    after = None
    nodes = []
    for page_count in range(1, pages):
        org_data = fetch_org_repos(organization, page_size, after)
        nodes.extend(collate(org_data))
        if nested_keys_exist(org_data, ["data", "organization", "repositories", "pageInfo", "endCursor" ]):
            page_info = org_data["data"]["organization"]["repositories"]["pageInfo"]
            after = page_info["endCursor"]
            has_next_page = page_info["hasNextPage"]
            if not has_next_page:
                break
    return nodes



def collate(query_response):
    try:
        nodes = query_response["data"]["organization"]["repositories"]["nodes"]
        return nodes
    except Exception as err:
        nested_keys_exist(query_response,
                          ["data", "organization", "repositories", "nodes"])
        print(f"Unexpected {err}")
        raise err
