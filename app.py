import os
from flask import Flask, render_template, request, redirect, url_for
from src.modules import github_api as github
from dotenv import load_dotenv
from src.models.UserMessage import UserMessage
from src.models import UserMessage

from src.modules.form import fetch_contact_data

app = Flask(__name__)

@app.route("/")
def home():
    """load github projects and show the homepage

    Returns:
        Response: homepage
    """
    repos = github.get_repos()

    return render_template("index.html", repos=repos)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    """save a message from the user into a databse

    Returns:
        Response: redirection to the homepage
    """

    return redirect(url_for("home"))

if __name__ == "__main__":
    load_dotenv()
    app.run()
