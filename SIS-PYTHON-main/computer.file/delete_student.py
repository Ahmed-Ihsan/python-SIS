from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from model import *
from datetime import datetime 

da1 = student.query.filter_by(id=id2).delete()
db.session.commit()