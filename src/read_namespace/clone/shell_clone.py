import os
from ..utils.check_dict import nested_keys_exist


def clone(name, url, to_folder):
    clone_cmd = f"git clone {url} {to_folder}/{name}"
    print(clone_cmd)
    os.system(clone_cmd)


def clone_list(nodes, to_folder, protocol_field="url", language=None):
    os.chdir(to_folder)
    check_list = ["primaryLanguage", "name"]
    for node in nodes:
        name = node["name"]
        url = node[protocol_field]
        if language and nested_keys_exist(node, check_list) and \
                node["primaryLanguage"]["name"].lower() == language.lower():
            clone(name, url, to_folder)
        elif not language:
            clone(name, url, to_folder)
