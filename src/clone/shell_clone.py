import sys
import os


def clone(git_url):
    clone_cmd = f"git clone {git_url}"


def clone_list(nodes, to_folder):
    os.chdir(to_folder)
    for node in nodes:
        print(node["name"])
        clone(node["url"])