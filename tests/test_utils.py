import pytest
from src.read_namespace.utils.check_dict import keys_exists


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
    assert keys_exists(response_data["passing"],
                       ["data", "organization", "repositories",
                        "nodes"]) == True


def test_keys_do_not_exist(response_data):
    assert keys_exists(response_data["failing"],
                       ["data", "organization", "repositories",
                        "nodes"]) == False
