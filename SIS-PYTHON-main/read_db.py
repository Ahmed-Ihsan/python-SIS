from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash
from model import *

def PassWord(string):
	new_pass=""
	for i in string:
		new_pass=new_pass+str(hex(ord(i)))
	return str(new_pass)

data = User.query.all()
for n in data:
   x=n.password
   print(x)
   a=check_password_hash(x , PassWord('admin'))
   print(a)
