from flask import Flask
from app.ext import db, migrate, session, email
from app.blueprints.pessoa import bp_pessoa
from app.blueprints.home import bp_home
from app.blueprints.login import bp_login


def create_app():
    app = Flask(__name__)
    app.config.from_object("config")

    # Extensions
    db.configure(app)
    migrate.configure(app)
    session.configure(app)
    email.configure(app)

    # Blueprints
    bp_home.configure(app)
    bp_pessoa.configure(app)
    bp_login.configure(app)


    return app
