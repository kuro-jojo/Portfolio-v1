import datetime
from dotenv import load_dotenv
import logging
import socket
import os
from flask import Flask, render_template, request, redirect, url_for
from logging.handlers import SysLogHandler

load_dotenv()

from src.models.UserMessage import UserMessage
from src.models import UserMessage
from src.modules.form import fetch_contact_data

app = Flask(__name__)
paperTrailAppUrl = os.getenv("PAPER_TRAIL_URL")
paperTrailAppPort = os.getenv("PAPER_TRAIL_PORT")

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///portfolio.db"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS '] = False
db = UserMessage.db
db.init_app(app)


@app.route("/")
def home():
    """Send to homepage"""
    log()
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


# @app.before_request
def init():
    """Initialize some configurations"""
    # create tables
    with app.app_context():
        db.create_all()


def log():
    """Logs message to a remote log viewer"""
    if not paperTrailAppUrl and not paperTrailAppPort:
        raise TypeError("An url and a port is requested")

    syslog = SysLogHandler(address=(paperTrailAppUrl, int(paperTrailAppPort)))
    syslog.addFilter(ContextFilter())
    format = "%(asctime)s %(hostname)s Portfolio-kuro-jojo: %(message)s"
    formatter = logging.Formatter(format, datefmt="%b %d %H:%M:%S")
    syslog.setFormatter(formatter)
    logger = logging.getLogger()
    logger.addHandler(syslog)
    logger.setLevel(logging.INFO)
    message = f"IP : {request.remote_addr} - Browser : {request.headers.get('User-Agent').split(' ')[0]} "
    logger.info(message)

class ContextFilter(logging.Filter):
    hostname = socket.gethostname()

    def filter(self, record):
        record.hostname = ContextFilter.hostname
        return True


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
