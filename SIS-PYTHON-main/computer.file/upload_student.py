from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from model import *
from datetime import datetime 

time=datetime(int(time[0:4]),int(time[5:7]), int(time[8:10]))
data23= student.query.filter_by(id=id2).update(dict(firstname=name3 ,lestname=name4 ,Direct_Date=time ,Email=email ,phonenumber=num_ph ,Address=address ,department=department ,level=level ))
db.session.commit()
