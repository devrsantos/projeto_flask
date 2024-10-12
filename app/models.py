from app import db  # Importa o objeto db do SQLAlchemy

class User(db.Model):
    """
    Modelo que representa a tabela 'user' no banco de dados.
    """
    id = db.Column(db.Integer, primary_key=True)  # Coluna 'id' do tipo inteiro, chave primária
    nome = db.Column(db.String(80), nullable=False)  # Coluna 'nome' do tipo string, não pode ser nulo

    def __repr__(self):
        """
        Representação do objeto User.
        """
        return '<User %r>' % self.nome  # Retorna uma string com o nome do usuário
