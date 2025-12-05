from setuptools import setup

setup(
    name="github-activity",
    version="0.1.10",
    py_modules=["cli", "github_events"],
    install_requires=[],
    entry_points={"console_scripts": ["gitact = cli:main"]},
)
