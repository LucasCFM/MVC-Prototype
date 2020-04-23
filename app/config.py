import logging, os


class BaseConfig(object):
    ENVIRONMENT = 'base'
    
    LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    LOG_LEVEL = logging.DEBUG
    LOG_SAVE = True
    LOG_FILENAME = 'app.log'

    DB_NAME = f'test.db'


class DevConfig(BaseConfig):
    ENVIRONMENT = 'development'


class ProdConfig(BaseConfig):
    ENVIRONMENT = 'production'

    LOG_LEVEL = logging.INFO
    
    SQLALCHEMY_DATABASE_URI = f'production.db'


class TestConfig(BaseConfig):
    ENVIRONMENT = 'test'
    
    LOG_SAVE = False


class Config():
    """ Class instance for singleton """

    class __Config():
        """ Private singleton class """
        def __init__(self, config: BaseConfig):
            self.config = config

    instance = None

    def __init__(self, config: BaseConfig = None):
        if not config and not Config.instance:
            raise Exception('Config singleton has not been set yet')
        if config:
            Config.instance = Config.__Config(config)
    
    @property
    def config_vars(self) -> BaseConfig:
        return Config.instance.config


def set_config_var(env_type='development'):
    print(f'Initializing config singleton for env: {env_type}')
    if 'dev' in env_type:
        Config(DevConfig)
    else:
        Config(ProdConfig)

set_config_var( os.getenv('ENV_TYPE', 'development') )
