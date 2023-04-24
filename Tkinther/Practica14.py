from tkinter import Tk, Button, Frame, messagebox
import tkinter as tk
from tkinter import *
from tkinter import ttk
from generarP14 import *

generar=generarP14()

def IngresarS():
    generar.Ingresar(int(varIngresar.get()))

def RetirarS():
    generar.Retirar(int(varRetirar.get()))

def ConsultarS():
    messagebox.showinfo("El saldo es: ",generar.getSaldo())

def DepositarS():
    generar.Depositar(int(varDepositar.get()))

ventana=Tk()
ventana.title("Caja Popular")
ventana.geometry("500x400")

panel=ttk.Notebook(ventana)
panel.pack(fill='both',expand='yes')
seccion1=ttk.Frame(panel)
seccion2=ttk.Frame(panel)
seccion3=ttk.Frame(panel)
seccion4=ttk.Frame(panel)
seccion5=ttk.Frame(panel)
# Seccion 1


varConsultar=tk.StringVar()
lblcuenta1=tk.Label(seccion1, text="Ingresa el numero de cuenta: ").pack()
txtcuenta1=tk.Entry(seccion1).pack()
lbltitular1=tk.Label(seccion1, text="Ingresa el titular: ").pack()
txttitular1=tk.Entry(seccion1).pack()
lbledad1=tk.Label(seccion1, text="Ingresa tu edad: ").pack()
txtedad1=tk.Entry(seccion1).pack()
botonConsultar= Button(seccion1,text="Consultar", bg="#b0f5e8", fg="black",command=ConsultarS).pack()

# Seccion 2
varIngresar=tk.StringVar()
lblcuenta2=tk.Label(seccion2, text="Ingresa el numero de cuenta: ").pack()
txtcuenta2=tk.Entry(seccion2).pack()
lblsaldo2=tk.Label(seccion2, text="Saldo a Ingresar: ").pack()
txtsaldo2=tk.Entry(seccion2, textvariable=varIngresar).pack()
botonIngresar= Button(seccion2,text="Ingresar", bg="#b0f5e8", fg="black", command=IngresarS).pack()

# Seccion 3
varRetirar=tk.StringVar()
lblcuenta3=tk.Label(seccion3, text="Ingresa el numero de cuenta: ").pack()
txtcuenta3=tk.Entry(seccion3).pack()
lblsaldo3=tk.Label(seccion3, text="Ingresa el saldo que desea retirar: ").pack()
txtsaldo3=tk.Entry(seccion3,textvariable=varRetirar).pack()
botonRetirar= Button(seccion3,text="Retirar", bg="#b0f5e8", fg="black",command=RetirarS).pack()

# Seccion 4
varDepositar=tk.StringVar()
lblcuenta4=tk.Label(seccion4, text="Ingresa el numero de cuenta: ").pack()
txtcuenta4=tk.Entry(seccion4).pack()
lbltitular4=tk.Label(seccion4, text="Ingresa el titular: ").pack()
txttitular4=tk.Entry(seccion4).pack()
lbledad4=tk.Label(seccion4, text="Ingresa tu edad: ").pack()
txtedad4=tk.Entry(seccion4).pack()
lblsaldo4=tk.Label(seccion4, text="Saldo que desea depositar: ").pack()
txtsaldo4=tk.Entry(seccion4, textvariable=varDepositar).pack()
botonDepositar= Button(seccion4,text="Depositar", bg="#b0f5e8", fg="black", command=DepositarS).pack()

panel.add(seccion1,text="Consultar")
panel.add(seccion2,text="Insertar")
panel.add(seccion3,text="Retirar")
panel.add(seccion4,text="Depositar")

ventana.mainloop()