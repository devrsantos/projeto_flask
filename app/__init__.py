from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import SECRET_KEY

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = SECRET_KEY
    from config import SQLALCHEMY_DATABASE_URI
      
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    
    db.init_app(app)

    from .routes import bp as routes_bp
    app.register_blueprint(routes_bp)

    with app.app_context():
        db.create_all()
    
    return app