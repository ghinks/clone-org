from src.read_namespace.query_github.fetch_org_repos import \
    collate

response = {"data": {"organization": {
    "repositories": {
        "pageInfo": {
            "endCursor": "Y3Vyc29yOnYyOpKkcnViec4FZeYV",
            "hasNextPage": False
        },
        "nodes": [
            {
                "name": ".github",
                "url": "https://github.com/kubernetes-client/.github"
            },
            {
                "name": "c",
                "url": "https://github.com/kubernetes-client/c"
            },
            {
                "name": "csharp",
                "url": "https://github.com/kubernetes-client/csharp"
            },
            {
                "name": "gen",
                "url": "https://github.com/kubernetes-client/gen"
            },
            {
                "name": "go",
                "url": "https://github.com/kubernetes-client/go"
            },
            {
                "name": "go-base",
                "url": "https://github.com/kubernetes-client/go-base"
            },
            {
                "name": "haskell",
                "url": "https://github.com/kubernetes-client/haskell"
            },
            {
                "name": "java",
                "url": "https://github.com/kubernetes-client/java"
            },
            {
                "name": "javascript",
                "url": "https://github.com/kubernetes-client/javascript"
            },
            {
                "name": "perl",
                "url": "https://github.com/kubernetes-client/perl"
            },
            {
                "name": "python",
                "url": "https://github.com/kubernetes-client/python"
            },
            {
                "name": "python-base",
                "url": "https://github.com/kubernetes-client/python-base"
            },
            {
                "name": "ruby",
                "url": "https://github.com/kubernetes-client/ruby"
            }
        ]
    }
}}}


def test_collate():
    test_org = "kubernetes-client"
    collated = collate(response)
    assert len(collated) == len(
        response["data"]["organization"]["repositories"]["nodes"])
