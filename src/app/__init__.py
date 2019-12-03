from flask import Flask
from src.app.ext import session, email, migrate, db
from src.app.blueprints.pessoa import bp_pessoa
from src.app.blueprints.home import bp_home
from src.app.blueprints.login import bp_login


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
