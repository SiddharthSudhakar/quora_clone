import os
import _set_local_envs as _set_


class BaseConfig(object):
    """Constants used throughout the application."""
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    _set_.import_env_vars(BASE_DIR) # Setting local environments

    # Mongo Settings
    MONGO_DBNAME = os.environ.get('MONGO_DBNAME')
    MONGO_URI = os.environ.get('MONGO_URI_DEVELOPMENT')

class Development(BaseConfig):
    """Default Flask configuration inherited by all environments. Use this for development environments."""
    DEBUG = True
    TESTING = False
    SECRET_KEY = "Development"
    # Mongo Settings
    MONGO_DBNAME = 'Quora_clone' # TODO-deployment replace with "os.environ.get('MONGO_DBNAME_DEVELOPMENT')"
    MONGO_URI = 'mongodb://localhost:27017/Quora_clone' # TODO-deployment replace with "os.environ.get('MONGO_URI_DEVELOPMENT')"


class Testing(BaseConfig):
    TESTING = True
    #Mongo Settings
    MONGO_DBNAME = os.environ.get('MONGO_DBNAME')
    MONGO_URI = os.environ.get('MONGO_URI_TESTING')


class Production(BaseConfig):
    DEBUG = False
    SECRET_KEY = "Production"
    # Mongo Settings
    MONGO_DBNAME = os.environ.get('MONGO_DBNAME')
    MONGO_URI = os.environ.get('MONGO_URI_PRODUCTION')