from src.read_namespace.main import tabulate_nodes

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
    ]
}


def test_tabulate():
    tabulate_nodes(response["nodes"], "https")
