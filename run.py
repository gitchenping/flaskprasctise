from project import *

  

from flask import make_response


app= create_app('default')


@app.route('/')
def index():
    return '<h1>hello flask!</h1>'


@app.route('/request') 
def rquest_index(): 
    user_agent = request.headers.get('User-Agent') 
    return '<p>Your browser is %s</p>' % user_agent

@app.route('/user/<name>')
def user(name):
	return '<h1>hello '+name+' !</h1>'


@app.route('/userpath/<path:name>')
def userpath(name):
	
        return '<h1> hello '+name+' !</h1>'


@app.route('/res') 
def respage(): 
    response = make_response('<h1>This document carries a cookie!</h1>') 
    response.set_cookie('answer', '42') 
    return response


#from project.admin.view import adminmodule_blueprint
#app.register_blueprint(adminmodule_blueprint,url_prefix='/admin')


if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True)

