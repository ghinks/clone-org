import os
from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport

token = os.getenv("GITHUB_TOKEN")
reqHeaders = {
    'Authorization': 'Bearer ' + token
}


def fetch_org_repos(organization):
    # Select your transport with a defined url endpoint
    transport = AIOHTTPTransport(url="https://api.github.com/graphql", headers=reqHeaders)

    # Create a GraphQL client using the defined transport
    client = Client(transport=transport, fetch_schema_from_transport=True)

    # Provide a GraphQL query
    testQueryText = """
    query { 
  viewer { 
    login
  }
}
    """
    queryText = """
query GetAllOrgRepos($login: String!, $first: Int = 100, $after: String = null) {
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
"""
    query = gql(queryText)

    params = {
        "login": organization
    }

    result = client.execute(query, variable_values=params)
    print(result)
    return result
