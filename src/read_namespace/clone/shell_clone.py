import os
from ..utils.check_dict import nested_keys_exist


def matches_given_language(languages, repo_language):
    for language in languages:
        if language.lower() == repo_language.lower():
            return True
    return False


def clone(name, url, to_folder):
    clone_cmd = f"git clone {url} {to_folder}/{name}"
    print(clone_cmd)
    os.system(clone_cmd)


def clone_list(nodes, to_folder, protocol_field="url", languages=[]):
    os.chdir(to_folder)
    check_list = ["primaryLanguage", "name"]
    for node in nodes:
        name = node["name"]
        url = node[protocol_field]
        if len(languages) == 0:
            clone(name, url, to_folder)
        if len(languages) > 0 and nested_keys_exist(node, check_list) and \
                matches_given_language(languages,
                                       node["primaryLanguage"]["name"]):
            clone(name, url, to_folder)
