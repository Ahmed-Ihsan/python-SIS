import os
import time
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect, url_for, flash ,send_from_directory ,session
from werkzeug.security import check_password_hash
from werkzeug.utils import secure_filename
from model import *
from datetime import datetime

def PassWord(string):
	new_pass=""
	for i in string:
		new_pass=new_pass+str(hex(ord(i)))
	return str(new_pass)

UPLOAD_FOLDER = os.path.join('static', 'upload_file')
app = Flask(__name__)
app.secret_key='Ahmed_0x3510d08771d53c1e0x320x310x32_ihsan'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database/db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
db = SQLAlchemy(app)

@app.route("/", methods=['GET', 'POST'])
def cover():
	return render_template('cover.html')

@app.route('/pdf/<number>')
def send_pdf(number):
	if 'username' in session:
		return send_from_directory( 'static/upload_file/',number+'.pdf')
	return redirect(url_for('login'))

@app.route('/profile_amd')
def profile_amd():
	if 'username' in session:
		if request.method == 'POST':
			data=mail.query.filter_by(name=name).all()
			return render_template('profile_amd.html', inf=data)
		data=mail.query.all()
		return render_template('profile_amd.html', inf=data)
	return redirect(url_for('login'))

@app.route('/received_file/<unit>')
def received_file(unit):
	if 'username' in session:
		data=mail.query.filter_by(To=unit).all()
		return render_template('profile_amd.html', inf=data)
	return redirect(url_for('login'))

@app.route('/send_file/<unit>')
def send_file(unit):
	if 'username' in session:
			data=mail.query.filter_by(From=unit).all()
			return render_template('profile_amd.html', inf=data)
	return redirect(url_for('login'))


@app.route('/logout')
def logout():
   session.pop('username', None)
   return redirect(url_for('login'))

@app.route("/Administrative_unit", methods=['GET', 'POST'])
def Administrative_unit():
	if 'username' in session:
		return render_template('Administrative_unit.html',inf=None)
	else:
		return redirect(url_for('login'))

@app.route("/Administrative_unit/<Import>", methods=['GET', 'POST'])
def Administrative_unit2(Import):
	if 'username' in session:
		if request.method == 'POST':
			if Import == 'send':
				f = request.files['file']
				if f != None:
					f.save(os.path.join(app.config['UPLOAD_FOLDER'],f.filename))
					save_file=os.path.join(app.config['UPLOAD_FOLDER'],f.filename)
					From=request.form['From']
					name=request.form['name']
					To=request.form['To']
					time=datetime.now()
					us=mail(path=save_file, name=name , Direct_Date=time , To=To , From=From )
					db.session.add(us)
					db.session.commit()
					return render_template('Administrative_unit.html',inf=Import)
			if Import == 'book':
				f = request.files['file']
				if f != None:
					f.save(os.path.join(app.config['UPLOAD_FOLDER'],f.filename))
					save_file=os.path.join(app.config['UPLOAD_FOLDER'],f.filename)
					name=request.form['name']
					data1=teacher.query.filter_by(name=name).all()
					time=request.form['time']
					time=datetime(int(time[0:4]),int(time[5:7]), int(time[8:10]))
					us=mail(teacher_id=data1.id , Vacations="None" , book_thi=save_file , Notice='None' , Punishment='None')
					db.session.add(us)
					db.session.commit()
					return render_template('Administrative_unit.html',inf=Import)
		return render_template('Administrative_unit.html',inf=Import)
	return redirect(url_for('login'))

@app.route("/Add_Degree", methods=['GET', 'POST'])
def Add_Degree():
	if 'username' in session:
		if request.method == 'POST':
				student_name=request.form['student_name']
				class_1=request.form['class1']
				class_2=request.form['class2']
				class_3=request.form['class3']
				class_4=request.form['class4']
				class_5=request.form['class5']
				class_6=request.form['class6']
				class_7=request.form['class7']
				class_8=request.form['class8']
				department=request.form['department']
				level=request.form['level']
				us=d(student_id=student_id ,student_name=student_name ,class_1=class_1 , class_2= class_2 , class_3=class_3 , class_4=class_4 , class_5=class_5 , class_6=class_6 , class_7=class_7 , class_8=class_8 , department=department)
				db.session.add(us)
				db.session.commit()
				return render_template('Add_Degree.html')
		return render_template('Add_Degree.html')
	return redirect(url_for('login'))

@app.route("/upl_inf_stu/<int:id1>", methods=['GET', 'POST'])
def upl_inf_stu(id1):
	if 'username' in session:
		if request.method == 'POST':
			    id2=id1
			    name3=request.form['name1']
			    name4=request.form['name2']
			    time=request.form['time']
			    email=request.form['email']
			    num_ph=request.form['num_ph']
			    address=request.form['address']
			    department=request.form['department']
			    level=request.form['level']
			    exec(open('computer.file/upload_student.py').read())
			    data1=student.query.filter_by(id=id1).all()
			    data2=student.query.all()
			    return render_template('search_student.html' , info_fil=data1,info_all=data2,deep=department)
		data2=student.query.all()
		data1=None
		return render_template('search_student.html',info_fil=data1,info_all=data2 , deep=department)
	return redirect(url_for('login'))

@app.route("/upl_inf_stu/delete/<department>/<int:id1>", methods=['GET', 'POST'])
def upl_inf_stu_delete(id1 , department):
	if 'username' in session:
		if request.method == 'POST':
			id2=id1
			exec(open('computer.file/delete_student.py').read())
			data2=student.query.all()
			data1=None
			return render_template('search_student.html',info_fil=data1,info_all=data2 , deep=department)
		data2=student.query.all()
		data1=None
		return render_template('search_student.html',info_fil=data1,info_all=data2 , deep=department)
	return redirect(url_for('login'))

@app.route("/upl_file/<department>/<int:id1>", methods=['GET', 'POST'])
def upl_file(id1 , department ):
	if 'username' in session:
		if request.method == 'POST':
			f = request.files['file']
			type_file = request.files['type_file']
			if f != None:
					f.save(os.path.join(app.config['UPLOAD_FOLDER'],f.filename))
					save_file=os.path.join(app.config['UPLOAD_FOLDER'],f.filename)
					us=student_file(student_id=id1,path=save_file, type_file=type_file ,department= department)
					db.session.add(us)
					db.session.commit()
					data2=student.query.all()
					data1=None
					return render_template('search_student.html',info_fil=data1,info_all=data2 , deep=department)
			else:
				data2=student.query.all()
				data1=None
				return render_template('search_student.html',info_fil=data1,info_all=data2 , deep=department)
		else:
			data2=student.query.all()
			data1=None
			return render_template('search_student.html',info_fil=data1,info_all=data2 , deep=department)
	return redirect(url_for('login'))

@app.route("/Show_Depa_inf/<depa>", methods=['GET', 'POST'])
def Show_Depa_inf(depa):
	if 'username' in session:
		data1=Department.query.all()
		return render_template('show_teacher.html',info_fil=data1 , deep=depa)
	return redirect(url_for('login'))

@app.route("/show_teacher", methods=['GET', 'POST'])
def show_teacher_all():
	if 'username' in session:
		data1=teacher.query.all()
		return render_template('show_teacher.html',info_fil=data1)
	return redirect(url_for('login'))

@app.route("/ADD_Depa", methods=['GET', 'POST'])
def ADD_Depa():
	if 'username' in session:
		if request.method == 'POST':
			names=request.form['names']
			day=request.form['day']
			cost=request.form['cost']
			level=request.form['level']
			data=Department(name=names , Day=day , cost=cost , level=level)
			db.session.add(data)
			db.session.commit()
			return render_template('Add_Depa.html')
		return render_template('Add_Depa.html')
	return redirect(url_for('login'))

@app.route("/ADD_Subjects", methods=['GET', 'POST'])
def ADD_Subjects():
	if 'username' in session:
		if request.method == 'POST':
			names=request.form['nameSubjects']
			day=request.form['Day']
			teacher=request.form['teacher']
			department=request.form['department']
			level=request.form['level']
			data=Subjects(nameSubjects=names , Day=day , teacher=cost ,department=department , level=level)
			db.session.add(data)
			db.session.commit()
			return render_template('ADD_Subjects.html')
		return render_template('ADD_Subjects.html')
	return redirect(url_for('login'))

@app.route("/ADD_teacher", methods=['GET', 'POST'])
def ADD_teacher():
	if 'username' in session:
		if request.method == 'POST':
			names=request.form['names']
			data=teacher(name=names)
			db.session.add(data)
			db.session.commit()
			return render_template('Add_teacher.html')
		return render_template('Add_teacher.html')
	return redirect(url_for('login'))

@app.route("/search_student/<dep12>", methods=['GET', 'POST'])
def search_student(dep12):
	if 'username' in session:
		if request.method == 'POST':
			data=request.form['search']
			data1=student.query.filter_by(id=data).all()
			data2=student.query.all()
			return render_template('search_student.html' , info_fil=data1,info_all=data2,deep=dep12)
		data2=student.query.all()
		data1=None
		return render_template('search_student.html',info_fil=data1,info_all=data2 , deep=dep12)
	return redirect(url_for('login'))

@app.route("/ADD_student/<Depa>", methods=['GET', 'POST'])
def ADD_student_DEB(Depa):
	if 'username' in session:
		if request.method == 'POST':
			name1=request.form['name1']
			name2=request.form['name2']
			Direct_Date = request.form['date_time']
			email=request.form['email']
			ph_num=request.form['ph_num']
			address=request.form['address']
			department=request.form['department']
			level=request.form['level']
			print(int(Direct_Date[1:4]))
			Direct_Date=datetime(int(Direct_Date[0:4]),int(Direct_Date[5:7]), int(Direct_Date[8:10]))
			data=student(firstname=name1 , lestname=name2 , Direct_Date=Direct_Date , Email=email , phonenumber=ph_num , Address=address , department=department , level=level )
			db.session.add(data)
			db.session.commit()
			return render_template('Add_student.html',dep=Depa)
		return render_template('Add_student.html',dep=Depa)
	return redirect(url_for('login'))

@app.route("/ADD_student", methods=['GET', 'POST'])
def ADD_student():
	if 'username' in session:
		if request.method == 'POST':
			name1=request.form['name1']
			name2=request.form['name2']
			Direct_Date = request.form['date_time']
			email=request.form['email']
			ph_num=request.form['ph_num']
			address=request.form['address']
			department=request.form['department']
			level=request.form['level']
			Direct_Date=datetime(int(Direct_Date[0:4]),int(Direct_Date[5:7]), int(Direct_Date[8:10]))
			print(Direct_Date)
			data=student(firstname=name1 , lestname=name2 , Direct_Date=Direct_Date , Email=email , phonenumber=ph_num , Address=address , department=department , level=level )
			db.session.add(data)
			db.session.commit()
			return render_template('Add_student.html',dep=None)
		return render_template('Add_student.html',dep=None)
	return redirect(url_for('login'))

@app.route("/depar/<Depa>", methods=['GET', 'POST'])
def started(Depa):
	if 'username' in session:
		try:
			data=student.query.filter_by(department =Depa).all()
			return render_template('Show_Depa.html' , inf_dep=[Depa] , data=data)
		except Exception as e:
			return render_template('Show_Depa.html' , inf_dep= [Depa])
	return redirect(url_for('login'))

@app.route("/login", methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		try:
			username=request.form['username']
			data=User.query.filter_by(username = username ).first()
			info=[data.id,data.username,data.department]
			password=request.form['password']
			if check_password_hash(data.password ,PassWord(password)):
				session['username'] = username
				if data.department == "admin":
					return redirect(url_for('admin'))
				elif data.department == 'Administrative_unit':
					return redirect(url_for('Administrative_unit'))
				elif data.department == 'unitname':
					count_s=student.query.count()
					count_t=teacher.query.count()
					count_d=Department.query.count()
					count_all=[count_s , count_t , 7]
					return render_template('stated.html', info=info , count=count_all)
				elif data.department == 'adding':
					return render_template('Add_student.html', dep=None )
			errer='errer in passsword or usear name'
			return render_template('login_page.html' ,e=errer)
		except Exception as e:
			return render_template('login_page.html' , e=e)
	else :
		return render_template('login_page.html')

@app.route("/admin", methods=['GET', 'POST'])
def admin():
	if 'username' in session:
		if not department_user :
			return redirect(url_for('login'))
		if request.method == 'POST':
			try:
				username=request.form['username']
				data=request.form['data']
				typ=request.form['type']
				department=request.form['department']
				if 'insert' in typ:
					us=User(username=username , password=data , department=department)
					db.session.add(us)
					db.session.commit()
					return render_template('admin_page.html' , ret='successfully')
				elif 'upload' in typ :
					global data_up , data_up2
					data_up = username
					data_up2 = data
					exec(open('admin.file/upload.py').read())
					return render_template('admin_page.html' , ret="successfully")
				elif 'delete' in typ:
					global data_dl
					data_dl = username
					exec(open('admin.file/delete.py').read())
					return render_template('admin_page.html' , ret="successfully")
				elif 'search' in typ:
					data = User.query.filter_by(username=username).all()
					return render_template('admin_page.html' , all_data=data ,ret='successfully')
			except Exception as e:
				return render_template('admin_page.html' , e=e)
		return render_template('admin_page.html')
	return redirect(url_for('login'))

'''@app.route("/upload_file", methods=['GET', 'POST'])
def upload():
	if 'username' in session:
	if request.method == 'POST':
		try:
			f = request.files['file']
			debartment = request.form['debartment']
			if f != None:
				f.save(os.path.join(app.config['UPLOAD_FOLDER'],f.filename))
				save_file=os.path.join(app.config['UPLOAD_FOLDER'],f.filename)
				us=savefile(path=save_file , department= debartment)
				db.session.add(us)
				db.session.commit()
			return render_template('admin_page.html' , e="successfully")
		except Exception as e:
			return render_template('admin_page.html' , e=e)
	return render_template('admin_page.html' , e='nathing')
'''
@app.route("/unit", methods=['GET', 'POST'])
def unit():
	if 'username' in session:
		if request.method == 'POST':
			try:
				print(1)
				try:
					f = request.files['file']
				except Exception as e:
					print(1)
				bookname=request.form['bookname']
				Title=request.form['Title']
				type_si=request.form['type_si']
				typ=request.form['type']
				department=request.form['department']
				if 'insert' in typ:
					try:
						if f != None:
							f.save(os.path.join(app.config['UPLOAD_FOLDER'],f.filename))
							#save_file=os.path.join(app.config['UPLOAD_FOLDER'],f.filename)
							us1=Bookname(book_number=bookname , nmaefile=f.filename ,type_si=type_si, Title=Title , department = department)
							db.session.add(us1)
							db.session.commit()
							return render_template('unit.html' , e='successfully',all_data='http:\\\\127.0.0.1:5000\\pdf\\start' ,department = department )
						return render_template('unit.html' , e='None' ,all_data='http:\\\\127.0.0.1:5000\\pdf\\start',department = department)
					except Exception as e:
					  print(e)
					  return render_template('unit.html' ,all_data='http:\\\\127.0.0.1:5000\\pdf\\start' , e=e )
				elif 'upload' in typ :
					global data_up , data_up2
					data_up = bookname
					data_up2 = data
					exec(open('computer.file/upload.py').read())
					return render_template('unit.html' , ret="successfully" , all_data='http:\\\\127.0.0.1:5000\\pdf\\start',department = department)
				elif 'delete' in typ:
					global data_dl
					data_dl = bookname
					exec(open('computer.file/delete.py').read())
					return render_template('unit.html' , ret="successfully" ,all_data='http:\\\\127.0.0.1:5000\\pdf\\start', department = department)
				elif 'search' in typ:
					c=None
					data=Bookname.query.filter_by(book_number = bookname ).first()
					c=data.nmaefile
					c = c.replace(".pdf","")
					return render_template('unit.html' , all_data='http:\\\\127.0.0.1:5000\\pdf\\'+c ,e='successfully 22', department = department)
			except Exception as e:
				return render_template('unit.html' , all_data='http:\\\\127.0.0.1:5000\\pdf\\start', e=e , department = department )
			except Exception as e:
				return render_template('unit.html',e=e ,all_data='http:\\\\127.0.0.1:5000\\pdf\\start' , department = department)
		return render_template('unit.html' ,all_data='http:\\\\127.0.0.1:5000\\pdf\\start')
	return redirect(url_for('login'))


@app.route("/SIA", methods=['GET', 'POST'])
def SIA():
	if 'username' in session:
		if request.method == 'POST':
			try:
				firstname=request.form['firstname']
				lestname=request.form['lestname']
				Email=request.form['Email']
				phonenumber=request.form['phonenumber']
				Address=request.form['Address']
				City=request.form['City']
				department=request.form['department']
				level=request.form['level']
				true=request.form['true']
				us=student(firstname=firstname , lestname= lestname , Email=Email , phonenumber=phonenumber , Address=Address , City=City , department=department , level=level)
				db.session.add(us)
				db.session.commit()
			except Exception as e:
				pass
		return render_template('ASI.html')
	return redirect(url_for('login'))

@app.route("/SDId", methods=['GET', 'POST'])
def SDId():
	if 'username' in session:
		if request.method == 'POST':
				student_id=request.form['search']
				print(student_id)
				data = student.query.get(student_id)
				student_name=data.firstname+" "+data.lestname
				class_1=request.form['class1']
				class_2=request.form['class2']
				class_3=request.form['class3']
				class_4=request.form['class4']
				class_5=request.form['class5']
				class_6=request.form['class6']
				class_7=request.form['class7']
				class_8=request.form['class8']
				department=request.form['department']
				us=d(student_id=student_id ,student_name=student_name ,class_1=class_1 , class_2= class_2 , class_3=class_3 , class_4=class_4 , class_5=class_5 , class_6=class_6 , class_7=class_7 , class_8=class_8 , department=department)
				db.session.add(us)
				db.session.commit()
				data = student.query.all()
				return render_template('SDI.html',student=data)
		data = student.query.all()
		return render_template('SDI.html',student=data)
	return redirect(url_for('login'))


@app.route("/SIS", methods=['GET', 'POST'])
def SIS():
	if 'username' in session:
		if request.method == 'POST':
			Search=request.form['search']
			data=student.query.filter_by(firstname = Search ).all()
			return render_template('SIS.html',info=data)
		data = student.query.all()
		return render_template('SIS.html',info=data)
	return redirect(url_for('login'))



@app.route("/SDI", methods=['GET', 'POST'])
def SDI():
	if 'username' in session:
		if request.method == 'POST':
				student_id=request.form['search']
				data=d.query.get(student_id)
				return render_template('SDIshow.html',student=data)
		data=d.query.all()
		return render_template('SDIshow.html',student=data)
	return redirect(url_for('login'))


'''@app.route("/SDI2", methods=['GET', 'POST'])
def SDI_():
	if 'username' in session:
	if request.method == 'POST':
			student_id=request.form['search']
			data=d.query.get(student_id)
			return render_template('SDI.html',student=data)
	data = student.query.all()
	return render_template('SDI.html',student=data)
'''

@app.route("/SDI/<int:id_>", methods=['GET', 'POST'])
def SDI_id(id_):
	if 'username' in session:
		data=d.query.filter_by(id=id_).all()
		return render_template('SDIshow.html',student=data)
	return redirect(url_for('login'))

@app.route("/CCR", methods=['GET', 'POST'])
def CCR():
	if 'username' in session:
		if request.method == 'POST':
			roomname=request.form['Roomname']
			roomcode=request.form['roomcode']
			id_=request.form['id']
			try:
				f = request.files['file']
				department = request.form['department']
				if f != None:
					f.save(os.path.join(app.config['UPLOAD_FOLDER'],f.filename))
					save_file=os.path.join(app.config['UPLOAD_FOLDER'],f.filename)
					us=CCR_(pathimage=save_file ,room_name=roomname,roomCode=roomcode ,department=department, userid=id_)
					db.session.add(us)
					db.session.commit()
				return render_template('CCR.html',e="successfully")
			except Exception as e:
				return render_template('CCR.html',e=e)
		return render_template('CCR.html',e="welcome")
	return redirect(url_for('login'))

@app.route("/CCR_show", methods=['GET', 'POST'])
def CCR_show():
	if 'username' in session:
		data=CCR_.query.all()
		data2=CCR_.query.count()
		d=[]
		for i in range(data2):
			data2=data2-1
			d.append(data[data2].id)
		return render_template('CCR_show.html' , room=data , d=d)
	return redirect(url_for('login'))

@app.route("/post", methods=['GET', 'POST'])
def post():
	if 'username' in session:
		if request.method == 'POST':
			Title=request.form['Title']
			text=request.form['text']
			id_=request.form['id']
			
			try:
				f = request.files['file']
				
				department = request.form['department']
				
				if f != None:
					f.save(os.path.join(app.config['UPLOAD_FOLDER'],f.filename))
					save_file=os.path.join(app.config['UPLOAD_FOLDER'],f.filename)
					
					us=postes(idus=id_,Title=Title,text=text ,filebath=save_file, command=" ", department= department)
					db.session.add(us)
					
					db.session.commit()
				return render_template('class.html')
			except Exception as e:
				print(e)
				return render_template('class.html')
		return render_template('class.html')
	return redirect(url_for('login'))

@app.route("/post1/<int:id_>", methods=['GET', 'POST'])
def post1(id_):
	if 'username' in session:
		data=postes.query.filter_by(idus=id_).all()
		return render_template('class_show.html' , post=data)
	return redirect(url_for('login'))

@app.route("/post2/<int:idroom>", methods=['GET', 'POST'])
def post2(idroom):
	if 'username' in session:
		data=postes.query.filter_by(id=idroom).all()
		return render_template('class_show.html' , post2=data)
	return redirect(url_for('login'))



if __name__ == '__main__':
	app.run(debug=True)
	