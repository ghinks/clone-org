import pytest

from src.read_github_namespace.graph.fetch_org_repos import fetch_org_repos

@pytest.mark.integration
def test_fetch():
    try:
        fetch_org_repos('kubernetes-client')
    except Exception:
        pytest.fail("Exception raised ...")