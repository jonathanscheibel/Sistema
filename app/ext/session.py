from flask_login import LoginManager

login_manager = LoginManager()


def configure(app):
    login_manager.init_app(app)
