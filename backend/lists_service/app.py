from flask import Flask
from flask_cors import CORS
from database import db
from routes import lists_bp


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lists.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    CORS(app)
    db.init_app(app)
    app.register_blueprint(lists_bp)

    with app.app_context():
        db.create_all()

    @app.route('/health')
    def health():
        return {'status': 'ok', 'service': 'lists'}

    return app

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5002))
    app = create_app()
    app.run(host='0.0.0.0', port=port, debug=False)