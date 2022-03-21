from flask import Flask

from entities.base import base
from controllers.test_controller import test_controller
from config import URL_PREFIX


app = Flask(__name__)

app.config.from_object('config')
app.register_blueprint(test_controller, url_prefix=f'{URL_PREFIX}/test')

base.init_app(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
