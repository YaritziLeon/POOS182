from tkinter import messagebox
from random import choice

class generar:
    def __init__(self,nom,ap,am,a,c):
        self.__nombre=nom
        self.__apellidoP=ap
        self.__apellidoM=am
        self.__año=a
        self.__carrera=c
    
    def matricula(self):
        
        
    
    
    
    
    
    
    def getNombre(self):
        return self.__nombre
    def setNombre(self,nom):
        self.__nombre=nom
    def getApellidoP(self):
        return self.__apellidoP
    def setApellidoP(self,ap):
        self.__apellidoP=ap
    def getApellidoM(self):
        return self.__apellidoM
    def setApellidoM(self,am):
        self.__apellidoM=am
    def getAño(self):
        return self.__año
    def setAño(self,a):
        self.__año=a
    def getCarrera(self):
        return self.__carrera
    def setCarrera(self,c):
        self.__carrera=c