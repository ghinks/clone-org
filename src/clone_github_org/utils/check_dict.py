def nested_keys_exist(dictionary, keys):
    """Detect if the nested key exists in the dictionary

    This is a general test allough intended for use with dictionaries
    created from json files. We cannot guarantee that the keys are going
    to be extant.

    Args:
        dictionory: a dictionary to be tested
        keys: the keychain to walk to test if all the names exist

    Returns: True or False
    """
    if type(dictionary) is not dict:
        raise TypeError("Dictionary type expected")
    if type(keys) is not list:
        raise TypeError(
            f"Dictionary {dictionary!r} was passed with non list set of keys")
    keys_found = []
    nested_dict = dictionary
    for key in keys:
        if key is None:
            return False
        try:
            if type(nested_dict) is not dict:
                raise KeyError(
                    "looks like you expected more nesting but we ran out")
            nested_dict = nested_dict[key]
            keys_found.append(key)
        except KeyError:
            return False
    return True
