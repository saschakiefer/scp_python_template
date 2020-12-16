import os


class Config:
    APP_SECRET = os.environ.get("APP_SECRET") or "hard to guess string"
    SECRET_KEY = APP_SECRET  # Required by Flask-WTF

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig,
}
