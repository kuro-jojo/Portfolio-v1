from flask_sqlalchemy import SQLAlchemy
import sqlalchemy as sa

db = SQLAlchemy()


class UserMessage(db.Model):
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(30))
    email = sa.Column(sa.String(30))
    message = sa.Column(sa.Text)

    def __init__(self, name:str, email:str, message:str):
        self.name = name
        self.email = email
        self.message = message