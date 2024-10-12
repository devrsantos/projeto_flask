from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import SECRET_KEY

db = SQLAlchemy()  # Inicializa o SQLAlchemy

def create_app():
    """
    Função para criar a instância da aplicação Flask.
    """
    app = Flask(__name__)
    app.config['SECRET_KEY'] = SECRET_KEY
    from config import SQLALCHEMY_DATABASE_URI
      
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    
    db.init_app(app)  # Inicializa o SQLAlchemy com a aplicação

    from app.routes import bp  # Importa o blueprint das rotas
    app.register_blueprint(bp)  # Registra o blueprint na aplicação

    with app.app_context():
        db.create_all()  # Cria as tabelas no banco de dados

    return app  # Retorna a instância da aplicação