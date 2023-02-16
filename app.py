from flask import Flask, render_template
from controllers import github_api as g

app = Flask('__name__')

@app.route('/')
def home():
    repos = g.get_repos()
    
    return render_template('index.html')