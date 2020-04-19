from project import *


@app.route('/request') 
def request_index(): 
    user_agent = request.headers.get('User-Agent') 
    return '<p>Your browser is %s</p>' % user_agent

@app.route('/user/<name>')
def user(name):
        return '<h1>hello '+name+' !</h1>'


if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True)
