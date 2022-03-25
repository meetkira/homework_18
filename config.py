from constants import DATABASE_FILE_PATH


class Config(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{DATABASE_FILE_PATH}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
