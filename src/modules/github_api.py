from github import Github
import os

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

def get_repos():

    g = Github(GITHUB_TOKEN)
    
    return [ repo for repo in g.get_user().get_starred()]    
