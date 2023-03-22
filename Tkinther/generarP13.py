from tkinter import messagebox
from random import choice

class generar:
    def __init__(self):
        self.__longitud
        self.__mayusculas
        self.__caracteres
        
    contra = ('0123456789abcdefghijklmnopqrstuvwxyz')
    mayus = ('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    carac = ('!"#$%&/()=?¡')
    
    def validarContraseña(self,contra,mayus,carac):
        