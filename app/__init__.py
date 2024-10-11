from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import SQLALCHEMY_DATABASE_URI

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    
    db.init_app(app)

    from .routes import bd as routes_bd
    app.register_blueprint(routes_bd)

    with app.app_context():
        db.create_all()
    
    return app