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
                        "nodes"]) == True


def test_keys_do_not_exist(response_data):
    assert nested_keys_exist(response_data["failing"],
                             ["data", "organization", "repositories",
                        "nodes"]) == False
