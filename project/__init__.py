
from flask import Flask
#from flask import redirect
app=Flask(__name__)

app.config['SECRET_KEY'] = 'hard 121 to guess string'

from flask.ext.bootstrap import Bootstrap
bootstrap=Bootstrap(app)

from .admin.view import adminmodule_blueprint
app.register_blueprint(adminmodule_blueprint,url_prefix='/admin')
