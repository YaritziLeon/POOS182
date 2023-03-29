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
#Metodo que usa mi objeto controlador para Buscar un Usuario
def ejecutaSelect():
    rsUsu=controlador.consultarUsuario(varBus.get())
    #Iteramos el contenido de la consulta y lo guardamos 
    for usu in rsUsu:
        cadena=str(usu[0])+" "+usu[1]+" "+usu[2]+" "+str(usu[3])
    
    if(rsUsu):
        messagebox.showinfo("Encontrado",cadena)
    else:
        messagebox.showinfo("No encontrado","El ususario no existe en la BD")

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
# Agregamos el boton a la pestaña 1
btnGuardar=Button(pest1,text="Guardar Usuarios",bg="#abf7d2",command=ejecutaInsert).pack()
# Pestaña 2: Buscar Usuario
titulo2=Label(pest2,text="Buscar Usuario", fg="#f788c7",font=("ALGERIAN",18)).pack()
varBus=tk.StringVar()
lblid=Label(pest2,text="Identificador de Usuarios: ").pack()
txtid=Entry(pest2,textvariable=varBus).pack()
# Agregamos el boton a la pestaña 2
btnBusqueda=Button(pest2,text="Buscar",bg="#abf7d2",command=ejecutaSelect).pack()

subBus=Label(pest2,text="Registrado",fg="Blue",font=("Modern",14)).pack()
textBus=tk.Text(pest2,height=5,width=52).pack()

#Agregamos nuestras pestañas
panel.add(pest1,text="Formulario de Usuarios")
panel.add(pest2,text="Buscar Usuario")
panel.add(pest3,text="Consultar Usuarios")
panel.add(pest4,text="Actualizar Usuario")

ventana.mainloop()