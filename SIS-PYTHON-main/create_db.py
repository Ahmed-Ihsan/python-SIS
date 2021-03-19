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
	array =['adding','هندسة تقنيات الحاسوب','Administrative_unit','هندسة الاجهزة الطبية','طب الاسنان','لغة العربية','قانون','تحليلات']
	for n in array:
		us11=Level( department= n  , level="رئيس فسم"  ,le_el="1234" )
		db.session.add(us11)
		us21=Level( department= n  , level="مقرر قسم"  ,le_el="123" )
		db.session.add(us21)
		us31=Level( department= n , level="استاذ"  ,le_el="12" )
		db.session.add(us31)
		us41=Level( department= n  , level="موظف " ,le_el="1")
		db.session.add(us41)
	us411=Level( department= "admin"  , level="admin " ,le_el="1234")
	db.session.add(us411)
	us1=User(username='ahmed0' , password=generate_password_hash(PassWord("admin")) , Level_id="1")
	db.session.add(us1)
	us2=User(username='ahmed1' , password=generate_password_hash(PassWord("admin")) , Level_id="33")
	db.session.add(us2)
	us3=User(username='ahmed2' , password=generate_password_hash(PassWord("admin")) , Level_id="5")
	db.session.add(us3)
	us4=User(username='ahmed3' , password=generate_password_hash(PassWord("admin")), Level_id="9")
	db.session.add(us4)
	db.session.commit()
	
if __name__ == "__main__":
    with app.app_context():
        main()
