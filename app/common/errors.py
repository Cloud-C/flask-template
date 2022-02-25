from flask import jsonify, Blueprint

error_bp = Blueprint('error', __name__)


@error_bp.app_errorhandler(Exception)
def handle_500_error(e):
    _schema = {
        'code': 500,
        'msg': 'Internal Server Error'
    }
    return jsonify(_schema), 500
