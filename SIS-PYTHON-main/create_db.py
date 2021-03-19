from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
from model import *

def PassWord(string):
	new_pass=""
	for i in string:
		new_pass=new_pass+str(hex(ord(i)))
	return str(new_pass)
	
def main():
	db.create_all()
	us=User(username='ahmed0' , password=generate_password_hash(PassWord("admin")) , department='adding'  , level="رئيس فسم"  ,le_el="1234"  )
	db.session.add(us)
	db.session.commit()
	us=User(username='ahmed1' , password=generate_password_hash(PassWord("admin")) , department='admin'  , level="amdin"  ,le_el="----" )
	db.session.add(us)
	db.session.commit()
	us=User(username='ahmed2' , password=generate_password_hash(PassWord("admin")) , department='هندسة تقنيات الحاسوب'  , level="رئيس فسم"  ,le_el="1234" )
	db.session.add(us)
	db.session.commit()
	us=User(username='ahmed3' , password=generate_password_hash(PassWord("admin")) , department='Administrative_unit'  , level="رئيس فسم"  ,le_el="1234" )
	db.session.add(us)
	db.session.commit()
	
if __name__ == "__main__":
    with app.app_context():
        main()
