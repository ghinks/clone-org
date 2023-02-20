from pprint import pprint as pp
from src.read_github_namespace.graph.fetch_org_repos import collate, fetch_org_repos
from src.clone.shell_clone import clone_list

if __name__ == "__main__":
    organization = "kubernetes-client"
    to_folder = "/Users/ghinks/temp/test-1"
    results = fetch_org_repos(organization)
    nodes = collate(results)
    pp(nodes)
    clone_list(nodes, to_folder, "sshUrl")
