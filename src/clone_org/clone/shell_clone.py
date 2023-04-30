import os


def matches_given_language(languages, repo_language):
    for language in languages:
        if language.lower() == repo_language.lower():
            return True
    return False


def clone(name, url, to_folder):
    clone_cmd = f"git clone {url} {to_folder}/{name}"
    print(clone_cmd)
    os.system(clone_cmd)


def clone_list(nodes, to_folder, protocol_field="url"):
    os.chdir(to_folder)
    for node in nodes:
        name = node["name"]
        url = node[protocol_field]
        clone(name, url, to_folder)
