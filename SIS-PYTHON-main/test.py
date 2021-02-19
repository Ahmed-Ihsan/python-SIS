from flask_wtf import FlaskForm
from wtforms import StringField
from flask_wtf.csrf import CSRFProtect
from wtforms.validators import DataRequired
from flask import Flask ,render_template , request, redirect

class MyForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])


app = Flask(__name__) 
csrf = CSRFProtect(app)

@app.route("/") 
def hello(): 
	form = MyForm()
	return render_template('test.html' , form=form)
  
if __name__ == "__main__": 
  app.run()