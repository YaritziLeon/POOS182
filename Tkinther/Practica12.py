from tkinter import Tk, Button, Frame, messagebox
import tkinter as tk
from tkinter import *
from generarP12 import *
import tkinter as tk

generar=generarP12()

def validar():
    generar.Comprobar(varCorreo.get(),varContraseña.get())

ventana=Tk()
ventana.title("Login")
ventana.geometry("300x150")

seccion1=Frame(ventana, bg="#fcbbfb")
seccion1.pack(expand=True,fill='both')

varCorreo=tk.StringVar()
correo=tk.Label(seccion1, text="Ingresa tu correo").pack()
correo1=tk.Entry(seccion1, width=30, textvariable=varCorreo).pack()

varContraseña=tk.StringVar()
contraseña=tk.Label(seccion1, text="Ingresa tu contraseña").pack()
contraseña1=tk.Entry(seccion1, width=30, textvariable=varContraseña, show="*").pack()

botonIngresar= Button(seccion1,text="Ingresar", bg="#b0f5e8", fg="black",command=validar).pack()

ventana.mainloop()