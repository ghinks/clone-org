Graph Query
===============

To query the github repo a valid personal access token is
required for use with the graph call.


The basic query is

``
query GetAllOrgRepos($login: String!, $first: Int!, $after: String) {
  organization(login: $login) {
    repositories(
      first: $first
      after: $after
      orderBy: {field: NAME, direction: ASC}
    ) {
      pageInfo {
        endCursor
        hasNextPage
      }
      nodes {
        name
        url
      }
    }
  }
}
``

This will return the nodes with the url and name. With these variables a sample result is given

``
{
  "login": "kubernetes-client",
  "first": 100,
  "after": null
}
``

Response from Github

``
{
  "data": {
    "organization": {
      "repositories": {
        "pageInfo": {
          "endCursor": "Y3Vyc29yOnYyOpKkcnViec4FZeYV",
          "hasNextPage": false
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
    }
  }
}
``