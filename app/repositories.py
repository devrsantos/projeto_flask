from app.models import User

class UserRepository:
    def __init__(self, db):
        self.db = db

    def criar_usuario(self, nome):
        user = User(nome=nome)
        self.db.session.add(user)
        self.db.session.commit()
        return user

    def listar_usuarios(self):
        return User.query.all()

    def obter_usuario_por_id(self, id):
        return User.query.get(id)

    def atualizar_usuario(self, user, nome):
        user.nome = nome
        self.db.session.commit()
        return user

    def excluir_usuario(self, user):
        self.db.session.delete(user)
        self.db.session.commit()