from default import Config
class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@127.0.0.1/hello'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DATABASE_HOST = '127.0.0.1'
    DATABASE_USER = ''
    DATABASE_PASSWORD = ''
    DATABASE_PORT = ''