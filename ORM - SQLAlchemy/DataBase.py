# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 17:08:00 2019

@author: furkan.karakulak
"""
from sqlalchemy import create_engine  
from sqlalchemy.orm import sessionmaker


db_string = "postgresql://postgres:123@localhost:5432/python"
db = create_engine(db_string) 
Session = sessionmaker(db)  
session = Session()

class DataBaseClass:
    

    def __init__(self):
        self.session = session
 
    def add(entity):
        session.add(entity)  
        session.commit()
        
        