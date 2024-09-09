from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_cors import CORS

db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()
cors = CORS()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(app)

    from app.routes import main
    app.register_blueprint(main)

    return app
