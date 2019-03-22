# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 17:01:40 2019

@author: furkan.karakulak
"""

from Models import Giris,Yeni
from DataBase import DataBaseClass



newValue = Giris( name="Mustafa Furkan", lastname="Karakulak") 
secondvalue = Yeni( wsim ="Erdem", soyisim="Nalbur" ) 


DataBaseClass.add(newValue)
DataBaseClass.add(secondvalue)