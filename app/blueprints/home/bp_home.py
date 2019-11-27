from flask import Blueprint, render_template, redirect, url_for
from flask_login.utils import _get_user

bp_app = Blueprint("bp_home", __name__, template_folder='view')


@bp_app.route("/")
@bp_app.route("/index")
@bp_app.route("/home")
def home():
    if _get_user().is_authenticated:
        return render_template("index.html")
    return redirect(url_for("bp_login.login"))


def configure(app):
    app.register_blueprint(bp_app)
