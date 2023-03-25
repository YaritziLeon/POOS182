from tkinter import *
from tkinter import ttk
import tkinter as tk
from webbrowser import get
from controladorBD import *

#Crear Instancia(Puente entre los dos archivos)
controlador= controladorBD()

#Metodo que usa mi objeto controlador para insertar
def ejecutaInsert():
    controlador.guardarUsuario(varNom.get(),varCor.get(),varCon.get())

ventana=Tk()
ventana.title("CRUD de usuarios")
ventana.geometry("500x300")
# Creamos nuestros panel
panel=ttk.Notebook(ventana)
panel.pack(fill='both',expand='yes')
#Creamos nuestras pestañas
pest1=ttk.Frame(panel)
pest2=ttk.Frame(panel)
pest3=ttk.Frame(panel)
pest4=ttk.Frame(panel)
# Pestaña 1: Formulario de Registro
titulo=Label(pest1,text="Registro Usuarios", fg="#f788c7",font=("ALGERIAN",18)).pack()
varNom=tk.StringVar()
lb1Nom=Label(pest1,text="Nombre: ").pack()
txtNom=Entry(pest1,textvariable=varNom).pack()
varCor=tk.StringVar()
lb1Cor=Label(pest1,text="Correo: ").pack()
txtCor=Entry(pest1,textvariable=varCor).pack()
varCon=tk.StringVar()
lb1Con=Label(pest1,text="Contraseña: ").pack()
txtCon=Entry(pest1,textvariable=varCon).pack()
# Agregamos el boton
btnGuardar=Button(pest1,text="Guardar Usuarios",bg="#abf7d2",command=ejecutaInsert).pack()
#Agregamos nuestras pestañas
panel.add(pest1,text="Formulario de Usuarios")
panel.add(pest2,text="Buscar Usuario")
panel.add(pest3,text="Consultar Usuarios")
panel.add(pest4,text="Actualizar Usuario")

ventana.mainloop()