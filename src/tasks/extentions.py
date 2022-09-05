
class Huey:
    __app = None
    __instance = None

    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        self.__app = app

        _config = app.config.get("HUEY")

        if not _config:
            raise Exception("Huey requires a configuration in `app.config`")

        if not isinstance(_config, dict):
            raise Exception("Huey expects a dictionary as its configuration")

        _huey_instance = self.init_huey(_config)

        app.extensions["huey"] = _huey_instance
        self.__instance = _huey_instance

    def init_huey(self, config):
        _huey = RedisHuey(
            name=config.get("name", self.__app.name),
            url=config.get("url", None),
            result_store=config.get("result_store", False),
            events=config.get("events", True),
            store_none=config.get("store_none", False),
            always_eager=config.get("always_eager", False),
            store_errors=config.get("store_errors", True),
            blocking=config.get("blocking", False),
            read_timeout=config.get("read_timeout", 1),
        )
        return _huey

    def __getattr__(self, name):
        return getattr(self.__instance, name, None)
      

huey = Huey()