import os

class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = '12345'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://mariga:password@localhost/blogposts'


# email config_options
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'aizakmariga@gmail.com'
    MAIL_PASSWORD = '@temporarypassword123'
    SUBJECT_PREFIX = 'thePitcher'
    SENDER_EMAIL = 'aizakmariga@gmail.com'

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

    if SQLALCHEMY_DATABASE_URI.startswith('postgres://'):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace('postgres://','postgresql://',1)
class DevConfig(Config):
    

    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig,
    # 'test': TestConfig

}
