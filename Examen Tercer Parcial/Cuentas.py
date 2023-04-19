from tkinter import *
from tkinter import ttk
import tkinter as tk






ventana=Tk()
ventana.title("Banco")
ventana.geometry("600x500")

panel=ttk.Notebook(ventana)
panel.pack(fill='both',expand='yes')

pestaña1=ttk.Frame(panel)
pestaña2=ttk.Frame(panel)
pestaña3=ttk.Frame(panel)

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
btnInsertar=Button(pestaña1,text="Insertar",bg="#b0bde8").pack()

panel.add(pestaña1,text="Insertar Cuenta")
panel.add(pestaña2,text="Actualizar Cuenta")
panel.add(pestaña3,text="Consultar Cuentas")

ventana.mainloop()