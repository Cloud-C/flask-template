from flask import Blueprint, jsonify

from app.services.my_service import MyService

home_bp = Blueprint('home', __name__)


@home_bp.route('/hi', methods=['GET'])
def hi():
    data = MyService.hi()
    return data
