import pytest

from src.read_namespace.query_github.fetch_org_repos import fetch_org_repos

@pytest.mark.integration
def test_fetch():
    try:
        fetch_org_repos('kubernetes-client')
    except Exception:
        pytest.fail("Exception raised ...")