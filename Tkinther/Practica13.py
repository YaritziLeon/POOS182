from tkinter import Tk, Button, Frame, messagebox
import tkinter as tk
from tkinter import *
from generarP13 import *

generar=generarP13()

def GenerarContraseña():
    generar.Contraseña(int(varLongitud.get()),varMayusculas.get(),varCaracteres.get())

ventana=Tk()
ventana.title("Password")
ventana.geometry("450x200")

seccion=Frame(ventana, bg="#fcbbfb")
seccion.pack(expand=True,fill='both')

varLongitud=tk.StringVar()
longitud=tk.Label(seccion, text="Ingresa la longitud de tu contraseña: ")
longitud.place(x=20, y=20)
longitud1=tk.Entry(seccion, width=30, textvariable=varLongitud)
longitud1.place(x=225, y=20)

varMayusculas=tk.StringVar()
mayusculas=tk.Label(seccion, text="¿Deseas incluir mayusculas?: ")
mayusculas.place(x=20, y=50)
mayusculas1=tk.Entry(seccion, width=30, textvariable=varMayusculas)
mayusculas1.place(x=185, y=50)

varCaracteres=tk.StringVar()
caracteres=tk.Label(seccion, text="¿Deseas incluir caracteres especiales?: ")
caracteres.place(x=20, y=80)
caracteres1=tk.Entry(seccion, width=30, textvariable=varCaracteres)
caracteres1.place(x=230, y=80)

botonGenerarValidar= Button(seccion,text="Generar y Validar", bg="#b0f5e8", fg="black", command=GenerarContraseña)
botonGenerarValidar.place(x=180,y=110, width=100, height=30)


ventana.mainloop()