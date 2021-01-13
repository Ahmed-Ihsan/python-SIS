from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from model import *

data = Department.query.all()
for n in data:
   x=n.id
   print(x)