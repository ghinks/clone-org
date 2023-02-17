import sys
import os


def clone(name, url, to_folder):
    clone_cmd = f"git clone {url} {to_folder}/{name}"
    print(clone_cmd)
    os.system(clone_cmd)


def clone_list(nodes, to_folder):
    os.chdir(to_folder)
    for node in nodes:
        name = node["name"]
        url = node["url"]
        clone(name, url, to_folder)