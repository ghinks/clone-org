import pytest
from src.read_namespace.arg_parsing.parse_cmd_line import get_url_type, \
    create_new_folder, get_toml_version
import os
import uuid


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


@pytest.mark.integration
def test_create_folder():
    to_folder = os.getcwd() + "/" + str(uuid.uuid4())
    try:
        create_new_folder(to_folder)
    except Exception as e:
        assert False, f"Exception was raised creating {to_folder} {e}"
    finally:
        if os.path.isdir(to_folder):
            os.rmdir(to_folder)


def test_read_toml():
    data = get_toml_version()
    print(data)
    assert data[:3] == "0.0"