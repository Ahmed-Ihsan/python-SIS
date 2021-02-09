from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database/db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

__tablename__ = "users"

class User( db.Model):
    """ User model """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    department= db.Column(db.String(), nullable=False)

class savefile(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	path = db.Column(db.String(), nullable=False)
	department = db.Column(db.String(), nullable=False)

#/////////////////////////////////////////////////////////////////////////////////#

class Subjects(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	nameSubjects= db.Column(db.String(), nullable=False)
	Day = db.Column(db.String(), nullable=False)
	teacher = db.Column(db.Integer, nullable=False)
	department = db.Column(db.String(), nullable=False)
	level = db.Column(db.String(), nullable=False)

class Bookname(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	book_number = db.Column(db.String(), nullable=False)
	path = db.Column(db.String(), nullable=False)
	department = db.Column(db.String(), nullable=False)

class student_file(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	path = db.Column(db.String(), nullable=False)
	student_id= db.Column(db.Integer, nullable=False)
	department = db.Column(db.String(), nullable=False)
	type_file = db.Column(db.String(), nullable=False)

class mail(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name_file=db.Column(db.String(), nullable=False)
	name= db.Column(db.String(), nullable=False)
	path = db.Column(db.String(), nullable=False)
	Direct_Date =db.Column(db.DateTime(), nullable=False)
	To = db.Column(db.String(), nullable=False)
	From = db.Column(db.String(), nullable=False)

class teacher(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name= db.Column(db.String(), nullable=False)

class teacher_inf(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	teacher_id= db.Column(db.Integer, nullable=False)
	Vacations=db.Column(db.String(), nullable=False)
	book_thi= db.Column(db.String(), nullable=False)
	Notice=db.Column(db.String(), nullable=False)
	Punishment=db.Column(db.String(), nullable=False)

class cost(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	departmentid = db.Column(db.String(), nullable=False)
	cost = db.Column(db.Integer, nullable=False)
	level = db.Column(db.String(), nullable=False)

class Department(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(), nullable=False)
	Day = db.Column(db.String(), nullable=False)
	cost = db.Column(db.Integer, nullable=False)
	teacher = db.Column(db.Integer, nullable=False)
	level = db.Column(db.String(), nullable=False)

class student(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	firstname = db.Column(db.String(), nullable=False)
	lestname = db.Column(db.String(), nullable=False)
	Direct_Date =db.Column(db.DateTime(), nullable=False)
	Email = db.Column(db.String(), nullable=False)
	phonenumber = db.Column(db.Integer, nullable=False)
	Address = db.Column(db.String(), nullable=False)
	department = db.Column(db.String(), nullable=False)
	level = db.Column(db.String(), nullable=False)

class d(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	student_name = db.Column(db.String(), nullable=False)
	class_1 = db.Column(db.String(), nullable=False)
	class_2 = db.Column(db.String(), nullable=False)
	class_3 = db.Column(db.String(), nullable=False)
	class_4 = db.Column(db.String(), nullable=False)
	class_5 = db.Column(db.String(), nullable=False)
	class_6 = db.Column(db.String(), nullable=False)
	class_7 = db.Column(db.String(), nullable=False)
	class_8 = db.Column(db.String(), nullable=False)
	Subjectsid = db.Column(db.Integer, nullable=False)
	department = db.Column(db.String(), nullable=False)
	level = db.Column(db.String(), nullable=False)

#//////////////////////////////////////////////////////////////////////////////#
class CCR_(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	pathimage= db.Column(db.String(), nullable=False)
	room_name=db.Column(db.String(), nullable=False)
	roomCode = db.Column(db.String(), nullable=False)
	department = db.Column(db.String(), nullable=False)
	userid=db.Column(db.Integer, nullable=False)

class postes(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	idus= db.Column(db.Integer, nullable=False)
	Title=db.Column(db.String(), nullable=False)
	text = db.Column(db.String(), nullable=False)
	filebath = db.Column(db.String(), nullable=False)
	command=db.Column(db.String(), nullable=False)
	department = db.Column(db.String(), nullable=False)
