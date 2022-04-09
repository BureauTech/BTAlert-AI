from flask import Blueprint

from services.test_service import prom


test_controller = Blueprint('test_controller', __name__)


@test_controller.route('/', methods=['GET'])
def get_test():
    try:
        return {'status': 200, 'success': True, 'data': prom.all_metrics()}
    except Exception as error:
        return {'status': 500, 'success': False, 'error': error}
