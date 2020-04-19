import os 
basedir = os.path.abspath(os.path.dirname(__file__)) 
 
class Config: 
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string' 
    
    @staticmethod 
    def init_app(app): 
        
        pass 
 
class DevelopmentConfig (Config): 
    DEBUG = True 
    MAIL_SERVER = 'smtp.googlemail.com' 
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') 
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') 

class TestingConfig (Config): 
    TESTING = True 
    
config = { 
    'development': DevelopmentConfig, 
    'testing': TestingConfig, 
    'default': DevelopmentConfig 
}
