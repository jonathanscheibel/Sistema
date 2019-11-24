from flask import Blueprint, render_template

bp_app = Blueprint("bp_home", __name__, template_folder='view')


@bp_app.route("/")
@bp_app.route("/home")
def home():
    return render_template("index.html")


def configure(app):
    app.register_blueprint(bp_app)
