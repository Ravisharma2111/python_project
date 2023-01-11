##OPEN API STUFF
OPENAI_API_KEY = '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'



## FLASK STUFF
class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = "this-is-a-super-secret-key"


config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}
