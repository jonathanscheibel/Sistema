from flask import Blueprint, render_template, redirect, url_for

from app.ext.db import db
from app.blueprints.pessoa.controller.cadastro import CadastroPessoa
from app.blueprints.pessoa.model.pessoa import Pessoa

bp_app = Blueprint("bp_pessoa", __name__, template_folder='view')


@bp_app.route("/cadastrar", methods=["GET", "POST"])
def cadastrar():
    form = CadastroPessoa()
    if form.validate_on_submit():
        p = Pessoa()
        form.populate_obj(p)
        db.session.add(p)
        db.session.commit()
        return redirect(url_for("bp_home.home"))
    return render_template("cadastro.html", form=form)


@bp_app.route("/lista")
def lista():
    pessoas = Pessoa.query.all()
    if pessoas:
        return render_template("lista.html", pessoas=pessoas)


@bp_app.route("/atualizar/<int:id>", methods=["GET", "POST"])
def atualizar(id):
    form = CadastroPessoa()
    pessoa = Pessoa.query.filter_by(_id=id).first()

    if form.validate_on_submit():
        form.populate_obj(pessoa)
        db.session.commit()

    form = CadastroPessoa()
    form.insert_data(pessoa)
    return render_template("atualizar.html", form=form)


@bp_app.route("/excluir/<int:id>")
def excluir(id):
    pessoa = Pessoa.query.filter_by(_id=id).first()
    db.session.delete(pessoa)
    db.session.commit()
    return redirect(url_for("bp_pessoa.lista"))


def configure(app):
    app.register_blueprint(bp_app)
