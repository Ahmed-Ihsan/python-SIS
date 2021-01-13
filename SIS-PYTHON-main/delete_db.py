from model import *
from sqlalchemy import *

engine = create_engine('sqlite:///database/db.sqlite')
'''table name'''
#input_N=input('Enter Teble Name')  
#input_N.__table__.drop(engine)
teacher.__table__.drop(engine)
CCR_.__table__.drop(engine)
postes.__table__.drop(engine)
d.__table__.drop(engine)
User.__table__.drop(engine)
savefile.__table__.drop(engine)
#Massage.__table__.drop(engine)
student.__table__.drop(engine)
Department.__table__.drop(engine)
Bookname.__table__.drop(engine)
Subjects.__table__.drop(engine)
