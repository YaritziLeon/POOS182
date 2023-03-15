from tkinter import Tk, Button, Frame, messagebox
import tkinter as tk

ventana=Tk()
ventana.title("Matricula")
ventana.geometry("400x300")

seccion=Frame(ventana, bg="#fcbbfb")
seccion.pack(expand=True,fill='both')

nombre=tk.Label(seccion, text="Ingresa tu Nombre:")
nombre.place(x=20, y=20)
nombre1=tk.Entry(seccion, width=30)
nombre1.place(x=125, y=20)
apellidoP=tk.Label(seccion, text="Ingresa tu Apellido Paterno:")
apellidoP.place(x=20, y=60)
apellidoP1=tk.Entry(seccion, width=30)
apellidoP1.place(x=170, y=60)
apellidoM=tk.Label(seccion, text="Ingresa tu Apellido Materno:")
apellidoM.place(x=20, y=100)
apellidoM1=tk.Entry(seccion, width=30)
apellidoM1.place(x=175, y=100)
año=tk.Label(seccion, text="Ingresa tu Año de Nacimiento:")
año.place(x=20, y=140)
año1=tk.Entry(seccion, width=30)
año1.place(x=185, y=140)
carrera=tk.Label(seccion, text="Ingresa tu Carrera:")
carrera.place(x=20, y=180)
carrera1=tk.Entry(seccion, width=30)
carrera1.place(x=120, y=180)

botonGenerar=Button(seccion,text="Generar",bg="white",fg="black")
botonGenerar.place(x=135,y=240, width=100, height=30)

ventana.mainloop()