from flask import Flask
from flask_cors import CORS
from database import db
from routes import products_bp


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
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
    app = create_app()
    app.run(port=5001, debug=True)