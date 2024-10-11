from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import User
from app import db
from app.repositories import UserRepository 

bp = Blueprint('routes', __name__, template_folder='templates')

user_repository = UserRepository(db)

@bp.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar_usuario():
    if request.method == 'POST':
        nome = request.form['nome']
        user_repository.criar_usuario(nome)
        return redirect(url_for('routes.listar_usuarios'))
    return render_template('index.html')

@bp.route('/listar')
def listar_usuarios():
    usuarios = user_repository.listar_usuarios()
    return render_template('listar.html', usuarios=usuarios)

@bp.route('/usuario/<int:id>')
def obter_usuario_por_id(id):
    usuario = user_repository.obter_usuario_por_id(id)
    if usuario:
        return render_template('usuario.html', usuario=usuario)
    else:
        flash('Usuario não encontrado.', 'danger')
        return redirect(url_for('routes.listar_usuarios'))