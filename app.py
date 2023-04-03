from dotenv import load_dotenv

load_dotenv()

import os
from flask import Flask, render_template, request, redirect, url_for
from src.modules import github_api as github
from src.models.UserMessage import UserMessage
from src.models import UserMessage

from src.modules.form import fetch_contact_data

app = Flask(__name__)

# app.config[
#     "SQLALCHEMY_DATABASE_URI"
# ] = f"mysql+pymysql://{ os.getenv('MYSQL_USER') }:{ os.getenv('MYSQL_PASSWORD')}@{ os.getenv('MYSQL_HOST')}/{ os.getenv('MYSQL_DATABASE')}"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///portfolio.db"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS '] = False
db = UserMessage.db
db.init_app(app)


@app.route("/")
def home():
    with open('user_visits.txt', 'a') as f:
        f.write(request.base_url)
        f.write('\n')
    return render_template("index.html")


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
            return "Message sent successfully ."
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
    app.run()