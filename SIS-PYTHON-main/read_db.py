from model import *

def PassWord(string):
	new_pass=""
	for i in string:
		new_pass=new_pass+str(hex(ord(i)))
	return str(new_pass)

data = Level.query.all()
a=[]
for n in data:
   print(n.department ,"      ",n.id,"  ", n.level,"   ",n.le_el)
   a.append(n.department)
a = list(dict.fromkeys(a))
print(a)
data = User.query.all()

print(n.username ,"      ",n.password , "   ", n.Level_id)
  
