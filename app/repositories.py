from app.models import User  # Importa o modelo User

class UserRepository:
    """
    Classe que representa o repositório de usuários.
    Responsável por realizar operações de acesso aos dados dos usuários.
    """
    def __init__(self, db):
        """
        Construtor da classe.
        Recebe o objeto db do SQLAlchemy como parâmetro.
        """
        self.db = db  # Armazena o objeto db

    def criar_usuario(self, nome):
        """
        Cria um novo usuário no banco de dados.
        Recebe o nome do usuário como parâmetro.
        Retorna o objeto User criado.
        """
        user = User(nome=nome)  # Cria um novo objeto User
        self.db.session.add(user)  # Adiciona o usuário à sessão
        self.db.session.commit()  # Salva as alterações no banco de dados
        return user  # Retorna o objeto User criado

    def listar_usuarios(self):
        """
        Retorna uma lista com todos os usuários do banco de dados.
        """
        return User.query.all()  # Retorna uma lista com todos os objetos User

    def obter_usuario_por_id(self, id):
        """
        Retorna o usuário com o ID especificado.
        Retorna None se o usuário não for encontrado.
        """
        return self.db.session.get(User, id)  # Retorna o objeto User com o ID especificado

    def atualizar_usuario(self, user, nome):
        """
        Atualiza o nome do usuário no banco de dados.
        Recebe o objeto User e o novo nome como parâmetros.
        Retorna o objeto User atualizado.
        """
        user.nome = nome  # Atualiza o nome do usuário
        self.db.session.commit()  # Salva as alterações no banco de dados
        return user  # Retorna o objeto User atualizado

    def excluir_usuario(self, user):
        """
        Exclui o usuário do banco de dados.
        Recebe o objeto User como parâmetro.
        """
        self.db.session.delete(user)  # Remove o usuário da sessão
        self.db.session.commit()  # Salva as alterações no banco de dados