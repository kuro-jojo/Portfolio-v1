import os
from flask import Flask, render_template, request, redirect, url_for
from src.modules import github_api as github
from dotenv import load_dotenv
from src.models.UserMessage import UserMessage
from src.models import UserMessage

from src.modules.form import fetch_contact_data

app = Flask(__name__)
print(os.getenv('MYSQL_USER'))
print(os.getenv('MYSQL_PASSWORD'))
print(os.getenv('MYSQL_HOST'))
print(os.getenv('MYSQL_DATABASE'))

app.config[
    "SQLALCHEMY_DATABASE_URI"
] = f"mysql+pymysql://{ os.getenv('MYSQL_USER') }:{ os.getenv('MYSQL_PASSWORD')}@{ os.getenv('MYSQL_HOST')}/{ os.getenv('MYSQL_DATABASE')}"
db = UserMessage.db
db.init_app(app)

print(os.getenv('MYSQL_USER'))
print(os.getenv('MYSQL_PASSWORD'))
print(os.getenv('MYSQL_HOST'))
print(os.getenv('MYSQL_DATABASE'))

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

    if request.method == "POST":
        try:
            userMessage = fetch_contact_data(request.form)
            db.session.add(userMessage)
            db.session.commit()
        except Exception as e:
            print(f"Exception found : {e}")
            return redirect(url_for("home"))

    return redirect(url_for("home"))


@app.before_first_request
def init():
    """Initialize some configurations"""

    # create tables
    with app.app_context():
        db.create_all()


if __name__ == "__main__":
    load_dotenv()
    app.run()
