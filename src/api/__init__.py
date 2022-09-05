
from flask import Blueprint, Flask, request
myflask_app = app = Blueprint('demo_api', __name__, url_prefix='/v1')

def install(app: Flask):
    # pylint: disable=W0404
    from .ping import api
    from .user import api
    app.register_blueprint(myflask_app)