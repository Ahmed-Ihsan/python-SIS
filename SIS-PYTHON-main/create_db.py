from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from model import *

def main():
	db.create_all()
	us=User(username='ahmed1' , password='admin' , department='admin')
	db.session.add(us)
	db.session.commit()
	us=User(username='ahmed2' , password='admin' , department='unitname')
	db.session.add(us)
	db.session.commit()
	
if __name__ == "__main__":
    with app.app_context():
        main()
