from flask import Flask

from flask import request  
from flask import Response

from .admin.view import adminmodule_blueprint

from config import config



def create_app(config_name): 
    app = Flask(__name__) 
    app.config.from_object(config[config_name]) 
    
    app.register_blueprint(adminmodule_blueprint,url_prefix='/admin') 
	
    return app

