from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    base_dir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(base_dir, '../instance/database.db')}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    Swagger(app)

    # Registrar rutas
    from .routes import main as main_blueprint, crypto_bp 
    app.register_blueprint(main_blueprint)
    app.register_blueprint(crypto_bp, url_prefix='/api')

    # Manejo de errores global
    @app.errorhandler(404)
    def not_found_error(error):
        return jsonify({'error': 'Resource not found'}), 404

    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({'error': 'Internal server error'}), 500

    return app
