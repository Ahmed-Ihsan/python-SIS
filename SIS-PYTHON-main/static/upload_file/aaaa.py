import tkinter as tk
import qrcode
import sqlite3
from sqlalchemy import *

metadata = MetaData()
engine = create_engine('sqlite:///db.sqlite')
conn = engine.connect()
users = Table('users', metadata,
	     Column('id', Integer, primary_key=True),
	     Column('name', String),
	     Column('number', Integer),
	     Column('code', String),
 )
metadata.create_all(engine)
ins = users.insert()
x=None

def print_text():
	# Create a SQL connection to our SQLite database
	con= sqlite3.connect("db.sqlite")
	cur = con.cursor()

	# The result of a "cursor.execute" can be iterated over by row
	f = open("db.txt", "a")
	for row in cur.execute('SELECT * FROM users;'):
		f.write(str(row)+"\n")
	f.close()

	# Be sure to close the connection
	con.close()
	res.configure(text = "تم استخراج البيانات ")

def QR(name , number , code):
	qr = qrcode.QRCode(

		        version=1,
		        error_correction=qrcode.constants.ERROR_CORRECT_L,
		        box_size=10,
		        border=4,
		    )
	qr.add_data("اسم القطعة :"+name+"\n عدد القطع :"+number+"\n الرمز: "+code)
	qr.make(fit=True)
	img = qr.make_image(fill_color="black", back_color="white")
	print(conn.execute(ins, { "name":name, "number": number , "code": code }))
	res.configure(text ="تم ادخال البيانات" )
	img.show()
	with open('myfile.png', 'wb') as f:
		img.save(f)


def read(name):
	# Create a SQL connection to our SQLite database
	con= sqlite3.connect("db.sqlite")
	cur = con.cursor()

	# The result of a "cursor.execute" can be iterated over by row
	for row in cur.execute('SELECT * FROM users;'):
		if name in row:
			con.close()
			return name
	con.close()
	return 0

def run():
	rea=read(variable.get())
	if rea :
		QR( variable.get() ,entry1.get()+rea,entry2.get())
	else:
		QR( variable.get() , entry1.get()+rea,entry2.get())
	return 0


if __name__ == '__main__':
	w = tk.Tk()
	w.geometry("300x250")
	w.title("كلية الحكمة الجامعة ")
	tk.Label(w, text="اسم المادة").pack()
	variable = tk.StringVar(w)
	variable.set("حاسبات")
	r = tk.OptionMenu(w, variable, "حاسبات", "طابعة", "راوتر")
	r.pack()
	tk.Label(w, text="العدد").pack()
	entry1 = tk.Entry(w,width=40)
	entry1.bind("<Return>", run)
	entry1.pack()
	tk.Label(w, text="الرمز").pack()
	entry2 = tk.Entry(w,width=40)
	entry2.bind("<Return>", run)
	entry2.pack()
	tk.Label(w, text=" ").pack()
	B = tk.Button(w, text ="استخراج البيانات", command = print_text)
	B.pack()
	res = tk.Label(w)
	res.pack()
	w.mainloop()