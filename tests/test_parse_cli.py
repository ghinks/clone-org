import pytest
from clone_org.arg_parsing.parse_cmd_line import get_url_type, \
    create_new_folder, split_languages
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


def test_split_languages():
    passing_list = [("java,braces", 2), ("python,c,c++", 3), ("c", 1),
                    ("c,cobol", 2), ("c,c++", 2), ("",0)]
    for languages, ln in passing_list:
        result = split_languages(languages)
        assert len(result) == ln
