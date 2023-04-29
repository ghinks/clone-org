from pathlib import Path
from setuptools import setup

cwd = Path(__file__).parent
long_description = (cwd / "README.md").read_text()

setup(
    long_description=long_description,
    long_description_content_type="text/markdown",
)