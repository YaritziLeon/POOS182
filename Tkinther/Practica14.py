from tkinter import Tk, Button, Frame, messagebox
import tkinter as tk

ventana=Tk()
ventana.title("Caja Popular")
ventana.geometry("470x200")

seccion=Frame(ventana, bg="#fcbbfb")
seccion.pack(expand=True,fill='both')

cuenta=tk.Label(seccion, text="Ingresa el numero de cuenta: ")
cuenta.place(x=20, y=20)
cuenta1=tk.Entry(seccion, width=30)
cuenta1.place(x=180, y=20)

titular=tk.Label(seccion, text="Ingresa el titular: ")
titular.place(x=20, y=50)
titular1=tk.Entry(seccion, width=30)
titular1.place(x=115, y=50)

edad=tk.Label(seccion, text="Ingresa tu edad: ")
edad.place(x=20, y=80)
edad1=tk.Entry(seccion, width=30)
edad1.place(x=110, y=80)

saldo=tk.Label(seccion, text="Ingresa el saldo: ")
saldo.place(x=20, y=110)
saldo1=tk.Entry(seccion, width=30)
saldo1.place(x=110, y=110)

botonConsultar= Button(seccion,text="Consultar", bg="#b0f5e8", fg="black")
botonConsultar.place(x=20,y=160, width=100, height=30)

botonIngresar= Button(seccion,text="Ingresar", bg="#b0f5e8", fg="black")
botonIngresar.place(x=130,y=160, width=100, height=30)

botonRetirar= Button(seccion,text="Retirar", bg="#b0f5e8", fg="black")
botonRetirar.place(x=240,y=160, width=100, height=30)

botonDepositar= Button(seccion,text="Depositar", bg="#b0f5e8", fg="black")
botonDepositar.place(x=350,y=160, width=100, height=30)

ventana.mainloop()