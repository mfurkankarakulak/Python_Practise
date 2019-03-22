# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 16:35:59 2019

@author: furkan.karakulak
"""

from sqlalchemy import create_engine  
from sqlalchemy import Column, String  
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import sessionmaker


# conn string
db_string = "postgresql://postgres:123@localhost:5432/python"

db = create_engine(db_string)  
base = declarative_base()

class Giris(base):  
    __tablename__ = 'giris'
    

    name = Column(String, primary_key=True)
    lastname = Column(String)

Session = sessionmaker(db)  
session = Session()

base.metadata.create_all(db)

# Create 
newValue = Giris( name="Allien", lastname="Derrickson")  
session.add(newValue)  
session.commit()

# Read
films = session.query(Giris)  
for film in films:  
    print(film.name)

"""
# Update
doctor_strange.title = "Some2016Film"  
session.commit()

# Delete
session.delete(doctor_strange)  
session.commit()  
"""