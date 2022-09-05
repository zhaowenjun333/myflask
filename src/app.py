


import flask
def get_app():
    app = flask.Flask(__name__, static_url_path='/v1/static')
    app.config.from_object('src.base_config')

    from .api import install as install_api
    install_api(app)
    from .task import huey
    install_task(app)
   


    return app



app= get_app()
