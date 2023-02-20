from src.arg_parsing.parse_cli import get_url_type

def test_get_url_type_ssh():
    test_fixture = {
        "prot": "ssh"
    }
    assert get_url_type(test_fixture) == "sshUrl"

def test_get_url_type_https():
    test_fixture = {
        "prot": "https"
    }
    assert get_url_type(test_fixture) == "url"
