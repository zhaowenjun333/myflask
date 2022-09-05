from .extensions import huey


def install(app: Flask):
    # pylint: disable=W0404

    huey.init_app(app)
    
    # app.register_blueprint(myflask_app)