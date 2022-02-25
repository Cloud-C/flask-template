from flask import Flask
from flask_cors import CORS

from app.common.errors import error_bp
from app.config import Config
from app.controllers.home_routes import home_bp
from app.controllers.kingdom_routes import kingdom_bp
from app.models.models import db
from app.schedulers.schedulers import scheduler


def _init_logger():
    """
        init logger
    """


def _init_db(_app):
    db.init_app(_app)


def init_scheduler(_app):
    scheduler.init_app(_app)
    scheduler.start()


def _register_routes(_app):
    _app.register_blueprint(home_bp)
    _app.register_blueprint(kingdom_bp)


def _register_error_handling(_app):
    _app.register_blueprint(error_bp)


def _register_probe(_app):
    @_app.route('/probe', methods=['GET'])
    def probe():
        return 'ok'


def _init_service(_app):
    """
        initial packages from third part
    """
    CORS(_app, resources={'*': {'origins': ['http://127.0.0.1']}})


def _init_params(_app):
    """
        initial specific params for global using
    """


def create_app():
    app = Flask(__name__)

    _config = Config()
    app.config.from_object(_config)

    _init_logger()
    _init_db(app)
    _init_params(app)
    _init_service(app)

    _register_error_handling(app)
    _register_routes(app)
    _register_probe(app)

    return app
