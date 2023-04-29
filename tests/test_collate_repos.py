from src.clone_github_org.query_github.fetch_org_repos import \
    collate, filter_by_language

response = {"data": {"organization": {
    "repositories": {
        "pageInfo": {
            "endCursor": "Y3Vyc29yOnYyOpKkcnViec4FZeYV",
            "hasNextPage": False
        },
        "nodes": [
            {
                "name": ".github",
                "url": "https://github.com/kubernetes-client/.github",
                "primaryLanguage": {
                    "name": "thing"
                }
            },
            {
                "name": "c",
                "url": "https://github.com/kubernetes-client/c",
                "primaryLanguage": {
                    "name": "c"
                }
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
                "url": "https://github.com/kubernetes-client/go",
                "primaryLanguage": {
                    "name": "Go"
                }
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
                "url": "https://github.com/kubernetes-client/python",
                "primaryLanguage": {
                    "name": "Python"
                }

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


def test_filter_by_language():
    test_org = "kubernetes-client"
    test_languages = ["python", "go"]
    collated = collate(response)
    filtered = filter_by_language(collated, test_languages)
    assert len(filtered) == 2
