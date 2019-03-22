# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 17:17:23 2019

@author: furkan.karakulak
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String  

base = declarative_base()

class Giris(base):  
   
    __tablename__ = 'giris'
    name = Column(String, primary_key=True)
    lastname = Column(String)
    
    
    def __init__(self,name,lastname):
        self.name = name
        self.lastname = lastname
    
    
class Yeni(base):
    
    __tablename__ = 'yeni'
    isim = Column(String, primary_key=True)
    soyisim = Column(String)
    
    def __init__(self,isim,soyisim):
        self.isim = isim
        self.soyisim = soyisim