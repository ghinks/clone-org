from src.read_namespace.query_github.fetch_org_repos import tabulate_nodes

response = {
    "nodes": [
        {
            "name": ".github",
            "url": "https://github.com/kubernetes-client/.github",
            "https": "a",
            "primaryLanguage": {
                "name": "Python"
            }
        },
        {
            "name": "c",
            "https": "b",
            "url": "https://github.com/kubernetes-client/c"
        },
        {
            "name": "d",
            "https": "e",
            "url": "https://github.com/kubernetes-client/c",
            "primaryLanguage": {
                "name": "Java"
            }
        },
    ]
}


def test_tabulate():
    tabulate_nodes(response["nodes"], "https")
    tabulate_nodes(response["nodes"], "https")
    tabulate_nodes(response["nodes"], "https")
