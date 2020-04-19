from flask import render_template
#from flask import Blueprint
from flask import redirect,url_for,session

from flask.ext.wtf import Form 
from wtforms import StringField, SubmitField,PasswordField
from wtforms.validators import Required,Length


from models import db,Customer

class MyForm(Form): 
    name = StringField('input your name?', validators=[Required()]) 

    password=PasswordField("input your password",validators=[Required(),Length(6,10,"password is not met")])
    submit = SubmitField('Submit') 



#adminmodule_blueprint = Blueprint('admin', __name__)

from . import adminmodule_blueprint
 


@adminmodule_blueprint.route('/login',methods=['GET', 'POST'])
def form_login():
    #return '<h1>this is admin blueprint</h1>'

    name = None
    myform = MyForm()
    if myform.validate_on_submit():
        name = myform.name.data
        password=myform.password.data
	
	myform.name.data=''
	myform.password.data = ''
	username=db.query(Customer).filter_by(Mobile_phone=name).first()
	
	if username is not None:

		session['name']=username.Nickname
		return redirect(url_for('admin.admin_index'))	
	else:
		name="no such username"

    return render_template('admin.html',form=myform,name=name)


@adminmodule_blueprint.route('/form',methods=['GET', 'POST'])
def form_index():
    #return '<h1>this is admin blueprint</h1>'

    name = None 
    myform = MyForm() 
    if myform.validate_on_submit(): 
        name = myform.name.data
	password=myform.password.data 
        myform.name.data = '' 
	myform.password.data = '' 
        session['name']=name
	return redirect(url_for('admin.admin_index'))

    return render_template('admin.html',form=myform,name=name)

 
@adminmodule_blueprint.route('/index')
def admin_index():
    return '<h1>this is admin blueprint</h1>'
    #return render_template('default.html',selfdefinestr="hello  "+session['name'] ,showonce=True)


@adminmodule_blueprint.route('/other')
def other_func():
	return "other function"





















