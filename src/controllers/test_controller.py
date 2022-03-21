from flask import Blueprint

from entities.base import base
from entities.test_entity import TestEntity


test_controller = Blueprint('test_controller', __name__)


@test_controller.route('/', methods=['GET'])
def get_test():
    try:
        data = base.session.query(TestEntity).all()
        print(data)
        return {'status': 200, 'success': True, 'data': len(data)}
    except Exception as error:
        return {'status': 500, 'success': False, 'error': error}
