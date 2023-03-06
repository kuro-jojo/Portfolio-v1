from github import Github
import os

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")


def get_repos():
    """get repositories from github using GitHub API

    Returns:
        list: a list of starred repositories
    """
    g = Github(GITHUB_TOKEN)

    return [repo for repo in g.get_user().get_starred()]
