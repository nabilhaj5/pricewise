

from flask import Flask
from flask_cors import CORS
from database import db
from routes import products_bp
import os


def create_app():
    app = Flask(__name__)

    # 1. Leer DATABASE_URL del entorno (Neon) o usar SQLite en local
    database_url = os.environ.get('DATABASE_URL', 'sqlite:///products.db')

    # 2. Normalizar postgres:// -> postgresql:// (algunos proveedores lo dan así)
    if database_url.startswith('postgres://'):
        database_url = database_url.replace('postgres://', 'postgresql://', 1)

    # 3. FORZAR el driver psycopg 3 para SQLAlchemy 2.1+
    if database_url.startswith('postgresql://'):
        database_url = database_url.replace('postgresql://', 'postgresql+psycopg://', 1)

    app.config['SQLALCHEMY_DATABASE_URI'] = database_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    CORS(app)
    db.init_app(app)
    app.register_blueprint(products_bp)

    with app.app_context():
        db.create_all()

    @app.route('/health')
    def health():
        return {'status': 'ok', 'service': 'products'}

    return app


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    app = create_app()
    app.run(host='0.0.0.0', port=port, debug=False)