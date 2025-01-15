from flask import Blueprint, Flask, render_template, request, redirect, url_for, session, flash, jsonify
from werkzeug.security import check_password_hash
from app.models import db, Usuario

main = Blueprint('main', __name__)

@main.route('/')
def login():
    return render_template('login.html')

@main.route('/login', methods=['POST'])
def login_post():
    username = request.form.get('name')
    password = request.form.get('password')

    user = Usuario.query.filter_by(nome=username).first()

    if not user or not check_password_hash(user.senha, password):
        flash("Usuário ou senha incorretos.")
        return redirect(url_for('main.login'))

    session['user_name'] = user.nome

    return redirect(url_for('main.dashboard'))

@main.route('/painel')
def dashboard():
    user_name = session.get('user_name', 'Usuário Desconhecido')
    return render_template('painel.html', user_name=user_name)

@main.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('main.login'))

@main.route('/usuarios')
def usuarios():
    return render_template('usuarios.html')

@main.route('/api/usuarios', methods=['GET'])
def get_usuarios():
    usuarios = Usuario.query.all()
    usuarios_dict = [
        {
            'id': usuario.id,
            'nome': usuario.nome,
            'ativo': usuario.ativo,
            'criado_at': usuario.criado_at.strftime('%d/%m/%Y %H:%M:%S'),
            'alterado_at': usuario.alterado_at.strftime('%d/%m/%Y %H:%M:%S') if usuario.alterado_at else None
        }
        for usuario in usuarios
    ]
    return jsonify(usuarios_dict)