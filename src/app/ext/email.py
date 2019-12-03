from flask_mail import Mail
import config

mail = Mail()


def configure(app):
    app.config['MAIL_SERVER'] = config.MAIL_SERVER
    app.config['MAIL_PORT'] = config.MAIL_PORT
    app.config['MAIL_USERNAME'] = config.MAIL_USERNAME
    app.config['MAIL_PASSWORD'] = config.MAIL_PASSWORD
    app.config['MAIL_USE_TLS'] = config.MAIL_USE_TLS
    app.config['MAIL_USE_SSL'] = config.MAIL_USE_SSL
    app.config['MAIL_DEFAULT_SENDER'] = config.MAIL_DEFAULT_SENDER
    mail.init_app(app)