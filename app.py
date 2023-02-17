from flask import Flask, render_template
from controllers import github_api as g
from dotenv import load_dotenv

app = Flask('__name__')

@app.route('/')
def home():
    repos = g.get_repos()
    for repo in repos:
        print(repo.clone_url)
    return render_template('index.html', repos=repos)


if __name__ == '__main__':
    load_dotenv()
    app.run()