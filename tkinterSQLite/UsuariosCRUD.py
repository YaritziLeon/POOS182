from tkinter import *
from tkinter import ttk
import tkinter as tk
from webbrowser import get
from controladorBD import *

#Crear Instancia(Puente entre los dos archivos)
controlador= controladorBD()

#Metodo que usa mi objeto controlador para insertar Pestaña 1
def ejecutaInsert():
    controlador.guardarUsuario(varNom.get(),varCor.get(),varCon.get())

#Metodo que usa mi objeto controlador para Buscar un Usuario Pestaña 2
def ejecutaSelect():
    rsUsu=controlador.buscarUsuario(varBus.get())
    
    #Iteramos el contenido de la consulta y lo guardamos 
    for usu in rsUsu:
        cadena=str(usu[0])+" "+usu[1]+" "+usu[2]+" "+str(usu[3])
    if(rsUsu):
        textBus.config(state='normal')
        textBus.delete(1.0,'end')
        textBus.insert('end',cadena)
        textBus.config(state='disabled')
        # messagebox.showinfo("Encontrado",cadena)
    else:
        messagebox.showinfo("No encontrado","El ususario no existe en la BD")

# Pestaña 3
def ejecuSelect():
    Cusu=controlador.consultarUsuario()
    tabla.delete(*tabla.get_children())
    for usuario in Cusu:
        cadena2=str(usuario[0])+" "+usuario[1]+" "+usuario[2]+" "+str(usuario[3])
        
        tabla.insert('',tk.END,text=usuario[0],values=cadena2)
        tabla.bind('<<TreeviewSelect>>',ejecuSelect)
        
        # messagebox.showinfo("Encontrado",cadena2)
    
# Pestaña 4
def ejecutaUpdate():
    actUsu=controlador.actualizarUsuario(varAct.get(),varNomb2.get(),varCorr2.get(),varCont2.get())
    for Musuario in actUsu:
        cadena3=str(Musuario[0])+" "+Musuario[1]+" "+Musuario[2]+" "+str(Musuario[3])
        
        tabla.update('',tk.END,values=cadena3)
        varNomb2.set(tabla.item('',"values")[1])
        varCorr2.set(tabla.item('',"values")[2])
        varCont2.set(tabla.item('',"values")[3])
        
        tabla.bind('<<TreeviewSelect>>',ejecutaUpdate)
        
    messagebox.showinfo("Listo","Se actualizo")
    
# Pestaña 5
def ejecutaDelete():
    confirmar=messagebox.askyesno('Pregunta','Confirma si quieres eliminar el usuario')
    if confirmar==True:
        controlador.eliminarUsuario(varEli.get())
    else:
        messagebox.showinfo('Listo','El usuario no ha sido eliminado')
    
    
ventana=Tk()
ventana.title("CRUD de usuarios")
ventana.geometry("700x500")
# Creamos nuestros panel
panel=ttk.Notebook(ventana)
panel.pack(fill='both',expand='yes')
#Creamos nuestras pestañas
pest1=ttk.Frame(panel)
pest2=ttk.Frame(panel)
pest3=ttk.Frame(panel)
pest4=ttk.Frame(panel)
pest5=ttk.Frame(panel)
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
textBus=tk.Text(pest2,height=5,width=52)
textBus.pack()

# Pestaña 3: Consultar Usuario
titulo3=Label(pest3,text="Consultar Usuario", fg="#f788c7",font=("ALGERIAN",18)).pack()
# Agregamos el boton a la pestaña 3
btnConsulta=Button(pest3,text="Consultar",bg="#abf7d2",command=ejecuSelect).pack()

subCon=Label(pest3,text="Usuarios Registrados",fg="Blue",font=("Modern",14)).pack()
textCon=tk.Text(pest3,height=10,width=60)
textCon.pack()

column=('num','nom','cor','con')
tabla=ttk.Treeview(textCon,columns=column,show='headings')
tabla.heading('num',text='Numero')
tabla.heading('nom',text='Nombre')
tabla.heading('cor',text='Correo')
tabla.heading('con',text='Contraseña')
tabla.pack()

# Pestaña 4: Actualizar Usuario
titulo4=Label(pest4,text="Actualizar Usuario", fg="#f788c7",font=("ALGERIAN",18)).pack()
varAct=tk.StringVar()
lblid2=Label(pest4,text="Id del Usuarios: ").pack()
txtid2=Entry(pest4,textvariable=varAct).pack()

varNomb2=tk.StringVar()
lblNomb2=Label(pest4,text="Nombre: ").pack()
txtNomb2=Entry(pest4,textvariable=varNomb2).pack()
varCorr2=tk.StringVar()
lblCorr2=Label(pest4,text="Correo: ").pack()
txtCorr2=Entry(pest4,textvariable=varCorr2).pack()
varCont2=tk.StringVar()
lblCont2=Label(pest4,text="Contraseña: ").pack()
txtCont2=Entry(pest4,textvariable=varCont2).pack()

# Agregamos el boton a la pestaña 4
btnActualizar=Button(pest4,text="Actualizar",bg="#abf7d2",command=ejecutaUpdate).pack()


# Pestaña 5: Eliminar Usuario
titulo5=Label(pest5,text="Eliminar Usuario", fg="#f788c7",font=("ALGERIAN",18)).pack()
varEli=tk.StringVar()
lblid3=Label(pest5,text="Identificador de Usuarios: ").pack()
txtid3=Entry(pest5,textvariable=varEli).pack()
# Agregamos el boton a la pestaña 5
btnEliminar=Button(pest5,text="Eliminar",bg="#abf7d2",command=ejecutaDelete).pack()

#Agregamos nuestras pestañas
panel.add(pest1,text="Formulario de Usuarios")
panel.add(pest2,text="Buscar Usuario")
panel.add(pest3,text="Consultar Usuarios")
panel.add(pest4,text="Actualizar Usuario")
panel.add(pest5,text="Eliminar Usuario")

ventana.mainloop()