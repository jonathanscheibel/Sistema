from flask import render_template, request, redirect, Blueprint, flash, url_for
from flask_login import login_user, logout_user
from flask_mail import Message
from app.ext.db import db
from app.ext.email import mail
from app.blueprints.login.model.user import User
from app.ext.utils.strings import get_random_string

bp_app = Blueprint("bp_login", __name__, template_folder='view')


@bp_app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        e_mail = request.form['email']
        pwd = request.form['password']
        user = User(name, e_mail, pwd)
        db.session.add(user)
        db.session.commit()
    return render_template('register.html')


@bp_app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        e_mail = request.form['email']
        pwd = request.form['password']
        user = User.query.filter_by(email=e_mail).first()
        if not user or not user.verify_password(pwd):
            return redirect('login')
        login_user(user)
        return redirect('home')
    return render_template('login.html')


@bp_app.route('/logout')
def logout():
    logout_user()
    return redirect('login')


@bp_app.route('/forgot', methods=["POST", "GET"])
def forgot():
    if request.method == "POST":
        email = request.form['mail']
        user = User.query.filter_by(email=email).first()
        if user:
            hash_code = get_random_string()
            user.hash_code = hash_code
            db.session.commit()
            msg = Message('Confirmação de alteração de senha', recipients=[email])
            msg.body = '''
Olá, você requisitou alteração de senha! 
Por gentileza, acesse o link ao lado para redefini-la: http://localhost:8000/''' + user.hash_code
            mail.send(msg)
            flash("Você receberá um email para redefinição de senha em alguns instantes!")
            return redirect('login')
        else:
            flash("Este email é inválido ou não está cadastrado.")
            return render_template('forgot_ask.html')
    else:
        return render_template('forgot_ask.html')


@bp_app.route("/<string:hash_code>", methods=["GET", "POST"])
def check_forgot(hash_code):
    user = User.query.filter_by(hash_code=hash_code).first()
    if user:
        if request.method == 'POST':
            passw1 = request.form['pw1']
            passw2 = request.form['pw2']
            if passw1 == passw2:
                user.password = user.generate_password(passw1)
                user.hash_code = None
                db.session.commit()
                return redirect(url_for('bp_login.login'))
            else:
                flash('As senhas não conferem!')
                return render_template('/forgot_check.html')
        else:
            return render_template('/forgot_check.html')
    else:
        return redirect('login')


def configure(app):
    app.register_blueprint(bp_app)
