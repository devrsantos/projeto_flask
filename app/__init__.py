from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meu_banco_de_dados.db'  
    
    db.init_app(app)

    from .routes import bd as routes_bd
    app.register_blueprint(routes_bd)

    with app.app_context():
        db.create_all()
    
    return app