class Config:
    DEBUG = False
    SECRET_KEY = 'sjhfjgdkflghmngkbdhjsghafcdgfsvhjbckngkmhl,lgfkdjghfxzbcnvmb,jkhfjgh'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:root@localhost/test'


class DevConfig(Config):
    DEBUG = True
