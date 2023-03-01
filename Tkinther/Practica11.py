from tkinter import Tk, Button, Frame, messagebox

#5. Agregar funcion de mensaje
def mostrarMensaje():
    messagebox.showinfo("Informacion", "Te informo que todo fallo con exito")
    messagebox.showerror("Error", "Fallo")
    print(messagebox.askokcancel("Pregunta", "¿Seguro que quieres guardar algo?"))
    print(messagebox.askyesno("Pregunta","¿Seguro que quieres salir?"))

#6.Funcion agregar botones
def agregarBoton():
    botonVerde.config(text="+", bg="green", fg="white")
    botonNuevo=Button(seccion3, text="Boton Nuevo")
    botonNuevo.pack()

#1. Generar una ventana 
ventana=Tk()
ventana.title("Practica 11")
ventana.geometry("600x400")

#2. Agregar Frames
seccion1=Frame(ventana, bg="#fcbbfb")
seccion1.pack(expand=True,fill='both')

seccion2=Frame(ventana, bg="#c3c6c7")
seccion2.pack(expand=True,fill='both')

seccion3=Frame(ventana, bg="#d79ef7")
seccion3.pack(expand=True,fill='both')

#3. Agregamos botones
botonAzul= Button(seccion1,text="Boton Azul", bg="#b0f5e8", fg="black", command=mostrarMensaje)
botonAzul.place(x=60,y=60, width=100, height=30)

botonNegro= Button(seccion2,text="Boton Negro", bg="black", fg="white")
botonNegro.grid(row=0, column=0)

botonRosa= Button(seccion2,text="Boton Rosa", bg="#fac3f6", fg="black")
botonRosa.grid(row=1, column=1)

botonVerde=Button(seccion3,text="Boton Verde", bg="#39fa60", fg="black",command=agregarBoton)
botonVerde.pack()

#4.Posicionamiento 

#Metodo main para la ejecucion de la ventana
ventana.mainloop()