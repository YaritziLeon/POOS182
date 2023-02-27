from tkinter import Tk, Button, Frame

#1. Generar una ventana 
ventana=Tk()
ventana.title("Practica 11")
ventana.geometry("600x400")

#2. Agregar Frames
seccion1=Frame(ventana, bg="red")
seccion1.pack(expand=True,fill='both')

seccion2=Frame(ventana, bg="gray")
seccion2.pack(expand=True,fill='both')

seccion3=Frame(ventana, bg="purple")
seccion3.pack(expand=True,fill='both')

#3. Agregamos botones
botonAzul= Button(seccion1,text="boton azul", bg="white", fg="blue")
botonAzul.place(x=60,y=60, width=100, height=30)

botonNegro= Button(seccion2,text="boton negro", bg="white", fg="black")
botonNegro.grid(row=0, column=0)

botonRosa= Button(seccion2,text="boton rosa", bg="black", fg="pink")
botonRosa.grid(row=1, column=1)

botonVerde=Button(seccion3,text="boton verde", bg="white", fg="green")
botonVerde.pack()

#Metodo main para la ejecucion de la ventana
ventana.mainloop()