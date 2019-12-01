from app import session
from app.ext.db import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


@session.login_manager.user_loader
def get_user(user_id):
    return User.query.filter_by(id=user_id).first()


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(86), nullable=False)
    email = db.Column(db.String(84), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    hash_code = db.Column(db.String(256))

    def __init__(self, name, email, password, hash_code):
        self.id = None
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)
        self.hash_code = hash_code
        self._is_authenticated = False
        self._is_active = True
        self._is_anonymous = False

    def verify_password(self, pwd):
        return check_password_hash(self.password, pwd)

    @staticmethod
    def generate_password(pwd):
        return generate_password_hash(pwd)