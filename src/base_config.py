DEBUG = True


# huey
settings__development = {
    'host': 'localhost'
}

settings__testing = {
    'host': 'localhost'
}

settings__production = {
    'host': 'production_server'
}

settings = {
    'development': settings__development,
    'testing': settings__testing,
    'production': settings__production,
    'default': settings__development
}