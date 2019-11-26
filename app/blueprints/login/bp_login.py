from flask import render_template, request, redirect, url_for, Blueprint
from flask_login import login_user, logout_user
from app.ext.db import db
from app.blueprints.login.model.user import User

bp_app = Blueprint("bp_login", __name__, template_folder='view')


@bp_app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        pwd = request.form['password']
        user = User(name, email, pwd)
        db.session.add(user)
        db.session.commit()
    return render_template('register.html')


@bp_app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        pwd = request.form['password']
        user = User.query.filter_by(email=email).first()
        if not user or not user.verify_password(pwd):
            return redirect('login')
        login_user(user)
        return redirect('home')
    return render_template('login.html')


@bp_app.route('/logout')
def logout():
    logout_user()
    return redirect('login')


def configure(app):
    app.register_blueprint(bp_app)