from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from model import *

data1 = Bookname.query.filter_by(name=data_dl).delete()
db.session.commit()
'''
data1 = User.query.all()
for q in data1:
 print(q.username)
 '''