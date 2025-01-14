from flask import Flask
from app.models import db
from app.routes import main

def create_app():
    app = Flask(__name__, template_folder="../templates", static_folder="../static")
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://AccessSystemAutoAlert:SystemAccessAutoAlert@localhost/autoalert'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = 'sua_chave_secreta_aqui'

    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(main)
    return app
