import pytest

from src.read_namespace.query_github.fetch_org_repos import fetch_org_repos, \
    fetch_num_org_repos, fetch_repo_by_page


@pytest.mark.integration
def test_fetch_repos():
    try:
        fetch_org_repos('kubernetes-client', 10, None)
    except Exception:
        pytest.fail("Exception raised ...")


@pytest.mark.integration
def test_fetch_count():
    """
    The resultant value comes back as
    {'organization': {'repositories': {'totalCount': 13}}}
    """
    try:
        fetch_num_org_repos('kubernetes-client')
    except Exception:
        pytest.fail("Exception raised ...")
@pytest.mark.integration
def test_fetch_by_pages():
    try:
        fetch_repo_by_page('kubernetes')
    except Exception:
        pytest.fail("Exception raised ...")
