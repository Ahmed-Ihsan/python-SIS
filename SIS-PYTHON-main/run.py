import os
import time
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect, url_for, flash ,send_from_directory ,session
from werkzeug.security import check_password_hash
from werkzeug.utils import secure_filename
from model import *
from datetime import datetime
from flask_sslify import SSLify
from OpenSSL import SSL

def PassWord(string):
	new_pass=""
	for i in string:
		new_pass=new_pass+str(hex(ord(i)))
	return str(new_pass)

UPLOAD_FOLDER = os.path.join('static', 'upload_file')
app = Flask(__name__)
context = ('web.crt', 'web.key')
sslify = SSLify(app)

app.secret_key='Ahmed_0x3510d08771d53c1e0x320x310x32_ihsan'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database/db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
db = SQLAlchemy(app)

@app.route("/route_section", methods=['GET', 'POST'])
@app.route("/route_section/<Type_path>", methods=['GET', 'POST'])
def route_section(Type_path=None):
	if  not('username' in session):
		return redirect(url_for('login'))
	elif request.method == 'POST':
		print(1)
		if Type_path in "add":
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
			return render_template('section_add.html')
		elif Type_path in "received_file":
			search=request.form['search']
			data=mail.query.filter_by(To=session['department'] , From=search).all()
			return render_template('sectionMailR.html',send=False, inf=data)
		elif Type_path in "send_file":
			search=request.form['search']
			data=mail.query.filter_by(From=session['department'] , To=search).all()
			return render_template('sectionMailS.html',send=True, inf=data)
	elif Type_path != None:
		if Type_path in "add":
			return render_template('section_add.html', db=session['department'] )
		elif Type_path in "search":
			    data2=student.query.all()
			    return render_template('section_editer.html',info_fil=None,info_all=data2 , deep=session['department'])
		elif Type_path in "received_file":
			data=mail.query.filter_by(To=session['department']).all()
			return render_template('sectionMailR.html',send=False, inf=data)
		elif Type_path in "send_file":
			data=mail.query.filter_by(From=session['department']).all()
			return render_template('sectionMailS.html',send=True, inf=data)
	else:
		data=student.query.filter_by(department=session['department']).all()
		return render_template('section_home.html' , data=data , db=session['department'] )

@app.route("/route_page", methods=['GET', 'POST'])
@app.route("/route_page/<Type_path>", methods=['GET', 'POST'])
def route_page(Type_path=None):
	if 'username' in session: 
		if "admin" in session['department']:
			if request.method == 'POST':
				print(Type_path)
				if Type_path == "send":
					f = request.files['file']
					if f != None:
						f.save(os.path.join(app.config['UPLOAD_FOLDER'],f.filename))
						save_file=os.path.join(app.config['UPLOAD_FOLDER'],f.filename)
						From=request.form['From']
						name=request.form['name']
						To=request.form['To']
						time=datetime.now()
						us=mail(path=save_file, name_file=f.filename , name=name , Direct_Date=time , To=To , From=From )
						db.session.add(us)
						db.session.commit()
						return render_template('admin_Send_mail.html')
				elif Type_path in "add":
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
					return render_template('admin_Add_studenat.html')
				search=request.form['search']
				Type=request.form['Type']
				section=request.form['section']
				if search == "":
					if Type in "2":
						data=mail.query.filter_by(From=section).all()
						return render_template('admin_sections.html',s=False, inf=data )
					elif Type in "1":
						data=mail.query.filter_by(To=section).all()
						return render_template('admin_sections.html',s=False, inf=data )
					else:
						data=student.query.filter_by(department=section).all()
						return render_template('admin_sections.html',s=True, inf=data )
			elif Type_path == None:
				data=mail.query.all()
				return render_template('admin_sections.html' , inf=data ,s=False)
			elif Type_path in "mail":
				data=mail.query.filter_by(To=Type_path).all()
				return render_template('admin_Mail.html', inf=data )
			elif Type_path in "send":
				return render_template('admin_Send_mail.html')
			else:
				return render_template('admin_Add_studenat.html')
	return redirect(url_for('login'))

# USES
@app.route("/route", methods=['GET', 'POST'])
def route():
	if 'هندسة تقنيات الحاسوب' in session['department']:
		try:
			data=student.query.filter_by(department= session['department']).all()
			return render_template('Show_Depa.html' , inf_dep=session['department'] , data=data)
		except Exception as e:
			return render_template('Show_Depa.html' , inf_dep=session['department'])
	return render_template('cover.html')

# USES
@app.route("/route_uint", methods=['GET', 'POST'])
def route_uint():
	if "Administrative_unit" in session['department']:
		return redirect(url_for('Administrative_unit'))
	return render_template('adding.html', inf = None )
# USES
@app.route("/SEND_uint", methods=['GET', 'POST'])
def SEND_uint():
	if "adding" in session['department']:
		if request.method == 'POST':
				f = request.files['file']
				if f != None:
					f.save(os.path.join(app.config['UPLOAD_FOLDER'],f.filename))
					save_file=os.path.join(app.config['UPLOAD_FOLDER'],f.filename)
					From=request.form['From']
					name=request.form['name']
					To=request.form['To']
					time=datetime.now()
					us=mail(path=save_file, name_file=f.filename , name=name , Direct_Date=time , To=To , From=From )
					db.session.add(us)
					db.session.commit()
					return redirect(url_for('route_uint'))
		return redirect(url_for('route_uint'))
	if request.method == 'POST':
				f = request.files['file']
				if f != None:
					f.save(os.path.join(app.config['UPLOAD_FOLDER'],f.filename))
					save_file=os.path.join(app.config['UPLOAD_FOLDER'],f.filename)
					From=request.form['From']
					name=request.form['name']
					To=request.form['To']
					time=datetime.now()
					us=mail(path=save_file,name_file=f.filename, name=name , Direct_Date=time , To=To , From=From )
					db.session.add(us)
					db.session.commit()
					return redirect(url_for('route'))
	return redirect(url_for('login'))


@app.route("/cover", methods=['GET', 'POST'])
def cover():
	inf = session['department']
	return render_template('cover.html' , inf=inf)

# USES
@app.route('/pdf/<number>')
def send_pdf(number):
	if 'username' in session:
		return send_from_directory(app.config['UPLOAD_FOLDER']+number+'.pdf')
	return redirect(url_for('login'))

# USES
@app.route('/profile_amd')
def profile_amd():
	if 'username' in session:
		if request.method == 'POST':
			data=mail.query.filter_by(name=name).all()
			return render_template('profile_amd.html', inf=data)
		data=mail.query.all()
		return render_template('profile_amd.html', inf=data)
	return redirect(url_for('login'))

# USES
@app.route('/received_file/<unit>' ,  methods=['GET', 'POST'])
def received_file(unit):
	if 'username' in session:
		if request.method == 'POST':
			search=request.form['search']
			data=mail.query.filter_by(To=unit , From=search ).all()
			return render_template('profile_amd.html',send=False, inf=data)
		if session['department'] in "adding":
				data=mail.query.filter_by(To='قسم التسجيل').all()
				return render_template('adding.html', inf=data)
		data=mail.query.filter_by(To=unit).all()
		return render_template('profile_amd.html',send=False, inf=data)
	return redirect(url_for('login'))

@app.route('/send_file/<unit>' ,  methods=['GET', 'POST'])
def send_file(unit):
	if 'username' in session:
			if request.method == 'POST':
				search=request.form['search']
				data=mail.query.filter_by(To=search , From=unit ).all()
				return render_template('profile_amd.html',send=True, inf=data)
			if session['department'] in "adding":
				data=mail.query.filter_by(From='قسم التسجيل').all()
				return render_template('adding.html', inf=data)
			data=mail.query.filter_by(From=unit).all()
			return render_template('profile_amd.html', send=True ,inf=data)
	return redirect(url_for('login'))

# USES
@app.route('/logout')
def logout():
   session.pop('username', None)
   session.pop('department', None)
   return redirect(url_for('login'))

# USES
@app.route("/Administrative_unit", methods=['GET', 'POST'])
def Administrative_unit():
	if 'username' in session:
		return render_template('Administrative_unit.html',inf=None)
	else:
		return redirect(url_for('login'))

# USES
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
			if Import == 'techer_inf':
				f = request.files['file']
				if f != None:
					f.save(os.path.join(app.config['UPLOAD_FOLDER'],f.filename))
					save_file=os.path.join(app.config['UPLOAD_FOLDER'],f.filename)
					name=request.form['name']
					data1=teacher.query.filter_by(name=name).all()
					if not data1:
						return render_template('Administrative_unit.html',inf=Import)
					time=request.form['time']
					note=request.form['note']
					Type=request.form['Type']
					time=datetime(int(time[0:4]),int(time[5:7]), int(time[8:10]))
					if "اجازة" in Type :
						us=teacher_inf(teacher_id=data1.id , Vacations=save_file , book_thi="None" , Notice=str(note) , Punishment='None')
					elif "عقوبات" in Type :
						us=teacher_inf(teacher_id=data1.id , Vacations='None' , book_thi="None" , Notice=str(note) , Punishment=save_file)
					else :
						us=teacher_inf(teacher_id=data1.id , Vacations='None' , book_thi=save_file , Notice=str(note) , Punishment='None')	
					db.session.add(us)
					db.session.commit()
					return render_template('Administrative_unit.html',inf=Import)
		return render_template('Administrative_unit.html',inf=Import)
	return redirect(url_for('login'))

# USES
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

# USES
@app.route("/upl_inf_stu/<int:id1>", methods=['GET', 'POST'])
def upl_inf_stu(id1):
	if 'username' in session:
		data2=student.query.all()
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
			    return render_template('section_editer.html' , info_fil=data1,info_all=data2,deep=department)
		data1=None
		return render_template('section_editer.html',info_fil=data1,info_all=data2 , deep=department)
	return redirect(url_for('login'))

# USES
@app.route("/upl_inf_stu/delete/<department>/<int:id1>", methods=['GET', 'POST'])
def upl_inf_stu_delete(id1 , department):
	if 'username' in session:
		if request.method == 'POST':
			id2=id1
			exec(open('computer.file/delete_student.py').read())
			data2=student.query.all()
			data1=None
			return render_template('section_editer.html',info_fil=data1,info_all=data2 , deep=department)
		data2=student.query.all()
		data1=None
		return render_template('section_editer.html',info_fil=data1,info_all=data2 , deep=department)
	return redirect(url_for('login'))

# USES
@app.route("/upl_file/<department>/<int:id1>", methods=['GET', 'POST'])
def upl_file(id1 , department ):
	if 'username' in session:
		if request.method == 'POST':
			f = request.files['file']
			type_file = request.form['typefile']
			if f != None:
					f.save(os.path.join(app.config['UPLOAD_FOLDER'],f.filename))
					save_file=os.path.join(app.config['UPLOAD_FOLDER'],f.filename)
					us=student_file(student_id=id1,path=save_file, type_file=type_file ,department= department)
					db.session.add(us)
					db.session.commit()
					data2=student.query.all()
					data1=None
					return render_template('section_editer.html',info_fil=data1,info_all=data2 , deep=department)
			else:
				data2=student.query.all()
				data1=None
				return render_template('section_editer.html',info_fil=data1,info_all=data2 , deep=department)
		else:
			data2=student.query.all()
			data1=None
			return render_template('section_editer.html',info_fil=data1,info_all=data2 , deep=department)
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

# USES
@app.route("/search_student/<dep12>", methods=['GET', 'POST'])
def search_student(dep12):
	if 'username' in session:
		if request.method == 'POST':
			data=request.form['search']
			data1=student.query.filter_by(id=data).all()
			data2=student.query.all()
			return render_template('section_editer.html' , info_fil=data1,info_all=data2,deep=dep12)
		data2=student.query.all()
		data1=None
		return render_template('section_editer.html',info_fil=data1,info_all=data2 , deep=dep12)
	return redirect(url_for('login'))


# USES
@app.route("/", methods=['GET', 'POST'])
@app.route("/login", methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		try:
			username=request.form['username']
			data=User.query.filter_by(username = username ).first()
			info=[data.id,data.username,data.department]
			password=request.form['password']
			if check_password_hash(data.password ,PassWord(password)):
				session['username']= username
				session['department']= data.department
				if session['department'] in "adding" or "Administrative_unit" in session['department']:
					return redirect(url_for('route_uint'))
				elif session['department'] in "admin":
					return redirect(url_for("route_page"))
				else:
					return redirect(url_for("route_section"))
				#if data.department == "admin":
					#return redirect(url_for('admin'))
				#elif data.department == 'Administrative_unit':
					#return redirect(url_for('Administrative_unit'))
				#elif data.department == 'unitname':
					#count_s=student.query.count()
					#count_t=teacher.query.count()
					#count_d=Department.query.count()
					#count_all=[count_s , count_t , 7]
					#return render_template('stated.html', info=info , count=count_all)
				#elif data.department == 'adding':
					#return render_template('Add_student.html', dep=None )
			errer='errer in passsword or usear name'
			return render_template('login_page.html' ,e=errer)
		except Exception as e:
			return render_template('login_page.html' , e=e)
	else :
		return render_template('login_page.html')

@app.route("/admin", methods=['GET', 'POST'])
def admin():
	if 'username' in session:
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

if __name__ == '__main__':
	#app.run(debug=True ,ssl_context=('cert.pem', 'key.pem'), host="0.0.0.0")
	#app.run(debug=True ,ssl_context=('cert.pem', 'key.pem'))
	app.run(debug=True , host="0.0.0.0")
	#--------CMD----------
	#set FLASK_APP=run
	#set FLASK_ENV=development
	#flask run