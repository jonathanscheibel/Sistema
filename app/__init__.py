from flask import Flask
from app.ext import db, migrate
from app.blueprints.pessoa import bp_pessoa
from app.blueprints.home import bp_home


def create_app():
    app = Flask(__name__)
    app.config.from_object("config")

    # Extensions
    db.configure(app)
    migrate.configure(app)

    # Blueprints
    bp_home.configure(app)
    bp_pessoa.configure(app)

    return app
