import os
import sys
from pathlib import Path
import json
from sgqlc.endpoint.http import HTTPEndpoint


# TODO create a unit test , look into [mock](https://pypi.org/project/pytest-asyncio/)

def fetch_org_repos(organization):
    token = os.getenv("GITHUB_TOKEN")
    headers = {
        'Authorization': 'Bearer ' + token
    }
    if not token:
        raise ValueError("No GITHUB_TOKEN in environment variables")
    url = 'https://api.github.com/graphql'
    # Provide a GraphQL query
    query = ""
    query_file = Path(__file__).with_name('org-repos.graphql')
    with query_file.open('r') as f:
        query = f.read()
    variables = {
        "login": organization
    }
    endpoint = HTTPEndpoint(url, headers)
    result = endpoint(query, variables)

    return result["data"]


def collate(data):
    try:
        nodes = data["organization"]["repositories"]["nodes"]
        return nodes
    except Exception as err:
        print(f"Unexpected {err}")
        raise err
