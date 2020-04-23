import logging

from flask import Flask

from app.config import Config
from app.router import api
from app.router.message import api as messageAPI

from app.db import db


CONFIG = Config().config_vars


def create_app(*args, **kwargs):
    print(f'Initializing app')
    app = Flask('mvc-prototype')

    # config app
    if 'dev' in CONFIG.ENVIRONMENT:
        app.config.from_object('app.config.DevConfig')
    elif 'prod' in CONFIG.ENVIRONMENT:
        app.config.from_object('app.config.ProdConfig')
    elif 'test' in CONFIG.ENVIRONMENT:
        app.config.from_object('app.config.TestConfig')
    print(f'App config has been sat')

    # register app routes
    app.register_blueprint(api)
    app.register_blueprint(messageAPI)

    # set logging
    logging.basicConfig(
        level=10,
        filename=CONFIG.LOG_FILENAME if CONFIG.LOG_SAVE else None,
        format=CONFIG.LOG_FORMAT
    )
    logger = logging.getLogger('api')
    logger.level = CONFIG.LOG_LEVEL
    print(f'App logging has been sat')

    @app.shell_context_processor
    def make_shell():
        return {'app': app, 'db': db}

    logging.info(f'App created')
    return app

    




