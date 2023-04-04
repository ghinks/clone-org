def nested_keys_exist(dictionary, keys):
    if type(dictionary) is not dict:
        raise TypeError("Dictionary type expected")
    if type(keys) is not list:
        raise TypeError(
            f"Dictionary {dictionary!r} was passed with non list set of keys")
    keys_found = []
    nested_dict = dictionary
    chain = ""
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
            if len(keys_found):
                for foundling in list(keys_found):
                    chain += f"{foundling}."
            print(f"keys found were {chain}, next key was MISSING")
            return False
    return True
