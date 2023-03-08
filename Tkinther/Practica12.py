from tkinter import Tk, Button, Frame, messagebox
import tkinter as tk

ventana=Tk()
ventana.title("Login")
ventana.geometry("400x300")

seccion1=Frame(ventana, bg="#fcbbfb")
seccion1.pack(expand=True,fill='both')

correo=tk.Label(seccion1, text="Ingresa tu correo")
correo.place(x=20, y=50)
contraseña=tk.Label(seccion1, text="Ingresa tu contraseña")
contraseña.place(x=20, y=100)

correo1=tk.Entry(seccion1, width=30)
correo1.place(x=170, y=50)
contraseña1=tk.Entry(seccion1, width=30)
contraseña1.place(x=170, y=100)

botonIngresar= Button(seccion1,text="Ingresar", bg="#b0f5e8", fg="black")
botonIngresar.place(x=50,y=250, width=100, height=30)

ventana.mainloop()