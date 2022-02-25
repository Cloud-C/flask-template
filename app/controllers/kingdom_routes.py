from flask import Blueprint

from app.services.my_service import MyService

kingdom_bp = Blueprint('kingdom', __name__)


@kingdom_bp.route('/who-r-u', methods=['GET'])
def who_r_u():
    data = MyService.who_r_u()
    return data
