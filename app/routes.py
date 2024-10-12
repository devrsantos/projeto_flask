from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import User
from app import db
from app.repositories import UserRepository

bp = Blueprint('routes', __name__, template_folder='templates')  # Cria um blueprint para as rotas

user_repository = UserRepository(db)  # Cria uma instância do UserRepository

@bp.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar_usuario():
    """
    Rota para cadastrar um novo usuário.
    """
    if request.method == 'POST':  # Se o método da requisição for POST
        nome = request.form['nome']  # Obtém o nome do formulário
        user_repository.criar_usuario(nome)  # Cria o usuário no banco de dados
        return redirect(url_for('routes.listar_usuarios'))  # Redireciona para a página de listar usuários
    return render_template('cadastrar.html')  # Renderiza o template de cadastro

@bp.route('/listar')
def listar_usuarios():
    """
    Rota para listar todos os usuários.
    """
    usuarios = user_repository.listar_usuarios()  # Obtém a lista de usuários do banco de dados
    return render_template('listar.html', usuarios=usuarios)  # Renderiza o template de listagem, passando a lista de usuários

@bp.route('/usuario/<int:id>')
def obter_usuario_por_id(id):
    """
    Rota para exibir as informações de um usuário específico.
    """
    usuario = user_repository.obter_usuario_por_id(id)  # Obtém o usuário do banco de dados pelo ID
    if usuario:  # Se o usuário for encontrado
        return render_template('usuario.html', usuario=usuario)  # Renderiza o template de detalhes do usuário
    else:  # Se o usuário não for encontrado
        flash('Usuário não encontrado.', 'danger')  # Exibe uma mensagem de erro
        return redirect(url_for('routes.listar_usuarios'))  # Redireciona para a página de listar usuários

@bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_usuario(id):
    """
    Rota para editar as informações de um usuário.
    """
    usuario = user_repository.obter_usuario_por_id(id)  # Obtém o usuário do banco de dados pelo ID
    if request.method == 'POST':  # Se o método da requisição for POST
        nome = request.form['nome']  # Obtém o novo nome do formulário
        user_repository.atualizar_usuario(usuario, nome)  # Atualiza o nome do usuário no banco de dados
        return redirect(url_for('routes.listar_usuarios'))  # Redireciona para a página de listar usuários
    return render_template('editar.html', usuario=usuario)  # Renderiza o template de edição, passando o usuário

@bp.route('/excluir/<int:id>')
def excluir_usuario(id):
    """
    Rota para excluir um usuário.
    """
    usuario = user_repository.obter_usuario_por_id(id)  # Obtém o usuário do banco de dados pelo ID
    if usuario:  # Se o usuário for encontrado
        user_repository.excluir_usuario(usuario)  # Exclui o usuário do banco de dados
        flash('Usuário excluído com sucesso!', 'success')  # Exibe uma mensagem de sucesso
    else:  # Se o usuário não for encontrado
        flash('Usuário não encontrado.', 'danger')  # Exibe uma mensagem de erro
    return redirect(url_for('routes.listar_usuarios'))  # Redireciona para a página de listar usuários
