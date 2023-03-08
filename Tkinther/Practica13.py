from tkinter import Tk, Button, Frame, messagebox
import tkinter as tk

ventana=Tk()
ventana.title("Password")
ventana.geometry("450x150")

seccion=Frame(ventana, bg="#fcbbfb")
seccion.pack(expand=True,fill='both')

longitud=tk.Label(seccion, text="Ingresa la longitud de tu contraseña: ")
longitud.place(x=20, y=20)
longitud1=tk.Entry(seccion, width=30)
longitud1.place(x=225, y=20)

mayusculas=tk.Label(seccion, text="¿Deseas incluir mayusculas?: ")
mayusculas.place(x=20, y=50)
mayusculas1=tk.Entry(seccion, width=30)
mayusculas1.place(x=185, y=50)

caracteres=tk.Label(seccion, text="¿Deseas incluir caracteres especiales?: ")
caracteres.place(x=20, y=80)
caracteres1=tk.Entry(seccion, width=30)
caracteres1.place(x=260, y=80)

botonGenerar= Button(seccion,text="Ingresar", bg="#b0f5e8", fg="black")
botonGenerar.place(x=180,y=110, width=100, height=30)

ventana.mainloop()