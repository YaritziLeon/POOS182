from tkinter import *
from tkinter import ttk
import tkinter as tk
from controladorBDBanco import *

controlador=controladorBDBanco()

def ejecutaInsertar():
    controlador.InsertarCuenta(varNCuenta.get(),varSaldo.get(),varNombre.get(),varCorreo.get())

def ejecutaActualizar():
    controlador.actualizarCuenta(varActualizar.get(),varNCuenta.get(),varSaldo.get(),varNombre.get(),varCorreo.get())
    messagebox.showinfo("Listo","Se actualizo")

def ejecutaConsultar():
    con=controlador.consultarCuentas()
    tabla.delete(*tabla.get_children())
    for cuentas in con:
        cadena1=str(cuentas[0])+" "+str(cuentas[1])+" "+str(cuentas[2])+" "+str(cuentas[3])
        
        tabla.insert('',tk.END,text=cuentas[0],values=cadena1)
        tabla.bind('<<TreeviewSelect>>',ejecutaConsultar)

ventana=Tk()
ventana.title("Banco")
ventana.geometry("600x500")

panel=ttk.Notebook(ventana)
panel.pack(fill='both',expand='yes')

pestaña1=ttk.Frame(panel)
pestaña2=ttk.Frame(panel)
pestaña3=ttk.Frame(panel)

#1
titulo1=Label(pestaña1,text="Insertar Cuenta", fg="#95aaf0",font=("ALGERIAN",16)).pack()
varNCuenta=tk.StringVar()
lb1NCuenta=Label(pestaña1,text="No de Cuenta: ").pack()
txtNCuenta=Entry(pestaña1,textvariable=varNCuenta).pack()
varSaldo=tk.StringVar()
lb1Saldo=Label(pestaña1,text="Saldo: ").pack()
txtSaldo=Entry(pestaña1,textvariable=varSaldo).pack()
varNombre=tk.StringVar()
lb1Nombre=Label(pestaña1,text="Nombre: ").pack()
txtNombre=Entry(pestaña1,textvariable=varNombre).pack()
varCorreo=tk.StringVar()
lb1Correo=Label(pestaña1,text="Correo: ").pack()
txtCorreo=Entry(pestaña1,textvariable=varCorreo).pack()
btnInsertar=Button(pestaña1,text="Insertar",bg="#b0bde8", command=ejecutaInsertar).pack()

#2
titulo2=Label(pestaña2,text="Actualizar Cuenta", fg="#95aaf0",font=("ALGERIAN",16)).pack()
varActualizar=tk.StringVar()
lblid=Label(pestaña2,text="Id de la Cuenta: ").pack()
txtid=Entry(pestaña2,textvariable=varActualizar).pack()

varNCuenta2=tk.StringVar()
lb1NCuenta2=Label(pestaña2,text="No de Cuenta: ").pack()
txtNCuenta2=Entry(pestaña2,textvariable=varNCuenta2).pack()
varSaldo2=tk.StringVar()
lb1Saldo2=Label(pestaña2,text="Saldo: ").pack()
txtSaldo2=Entry(pestaña2,textvariable=varSaldo2).pack()
varNombre2=tk.StringVar()
lb1Nombre2=Label(pestaña2,text="Nombre: ").pack()
txtNombre2=Entry(pestaña2,textvariable=varNombre2).pack()
varCorreo2=tk.StringVar()
lb1Correo2=Label(pestaña2,text="Correo: ").pack()
txtCorreo2=Entry(pestaña2,textvariable=varCorreo2).pack()
btnACtualizar=Button(pestaña2,text="Actualizar",bg="#b0bde8", command=ejecutaActualizar).pack()


#3
titulo3=Label(pestaña3,text="Consultar Cuentas", fg="#95aaf0",font=("ALGERIAN",16)).pack()
btnConsultar=Button(pestaña3,text="Consultar",bg="#b0bde8", command=ejecutaConsultar).pack()

subConsultar=Label(pestaña3,text="Cuentas",fg="#f799c7",font=("Modern",12)).pack()
textConsultar=tk.Text(pestaña3,height=10,width=60)
textConsultar.pack()

column=('id','num','sal','nom','cor')
tabla=ttk.Treeview(textConsultar,columns=column,show='headings')
tabla.heading('id',text='ID')
tabla.heading('num',text='No de Cuenta')
tabla.heading('sal',text='Saldo')
tabla.heading('nom',text='Nombre')
tabla.heading('cor',text='Correo')
tabla.pack()


panel.add(pestaña1,text="Insertar Cuenta")
panel.add(pestaña2,text="Actualizar Cuenta")
panel.add(pestaña3,text="Consultar Cuentas")

ventana.mainloop()