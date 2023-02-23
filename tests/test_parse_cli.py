from src.read_namespace.arg_parsing.parse_cmd_line import get_url_type


class ArgueTestFixture:
    def __init__(self, prot):
        self._prot = prot

    @property
    def protocol(self):
        return self._prot


def test_get_url_type_ssh():
    test_fixture = ArgueTestFixture("ssh")
    assert get_url_type(test_fixture) == "sshUrl"


def test_get_url_type_https():
    test_fixture = ArgueTestFixture("https")
    assert get_url_type(test_fixture) == "url"
