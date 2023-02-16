from github import Github


def get_repos():
    
    # First create a Github instance:

    # using an access token
    g = Github("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")
    
    return [ repo for repo in g.get_user().get_starred()]
    