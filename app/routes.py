from flask import Blueprint, render_template, request
from .models import User
from app import db

bd = Blueprint('routes', __name__, template_folder='templates')

@bd.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nome = request.form['nome']
        user = User(nome=nome)
        db.session.add(user)
        db.session.commit()
        return f'Olá, {nome}'
    return render_template('index.html')