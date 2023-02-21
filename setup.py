import setuptools

setuptools.setup(
    name="read_github_namespace",
    version="0.0.1",
    description="A tool to clone all the repos in a github organization for grep purposes",
    packages=setuptools.find_packages('src'),
    package_dir={"": "src"}
)
