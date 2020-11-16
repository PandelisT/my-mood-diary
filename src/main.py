# Loading environment variables
from dotenv import load_dotenv
load_dotenv()

# Flask application creation
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate

# used in other files
db = SQLAlchemy()
ma = Marshmallow()
bcrypt = Bcrypt()
jwt = JWTManager()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object("default_settings.app_config")

    # register db and marshmallow on app
    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)

    from commands import db_commands
    app.register_blueprint(db_commands)

    #Controller registration
    from controllers import registerable_controllers
    for controller in registerable_controllers:
        app.register_blueprint(controller)

    # error handler for bad request (e.g. no title included in post request)
    from marshmallow.exceptions import ValidationError
    @app.errorhandler(ValidationError)
    def handle_bad_request(error):
        return (jsonify(error.messages), 400)

    return app