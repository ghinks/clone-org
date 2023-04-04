import pytest
from src.read_namespace.utils.check_dict import nested_keys_exist


@pytest.fixture()
def response_data():
    return {
        "passing": {
            "data": {
                "organization": {
                    "repositories": {
                        "nodes": [1, 2, 3]
                    }
                }
            }
        },
        "failing": {
            "data": {
                "organization": {
                    "repositories": {
                        "things": [1, 2, 3]
                    }
                }
            }
        }
    }


def test_keys_exist(response_data):
    assert nested_keys_exist(response_data["passing"],
                             ["data", "organization", "repositories",
                              "nodes"]) is True


def test_keys_do_not_exist(response_data):
    assert nested_keys_exist(response_data["failing"],
                             ["data", "organization", "repositories",
                              "nodes"]) is False


def test_keys_with_empty_list(response_data):
    assert nested_keys_exist(response_data["passing"], []) is True


def test_keys_with_no_list(response_data):
    with pytest.raises(TypeError):
        nested_keys_exist(response_data["passing"], None)


def test_keys_with_none_in_list(response_data):
    assert nested_keys_exist(response_data["passing"], [None]) is False


def test_no_node(response_data):
    with pytest.raises(TypeError):
        nested_keys_exist(None, ["abc"])

def test_empty_dict():
    empty_dict = {"key": None}
    assert nested_keys_exist(empty_dict, ["key"]) is True

def test_none_dict():
    assert nested_keys_exist(None, ["a"]) is False

def test_none_dict():
    dict_with_no_dict_top_level = {
        "top": None
    }
    assert nested_keys_exist(dict_with_no_dict_top_level, ["top", "bottom"]) is False
