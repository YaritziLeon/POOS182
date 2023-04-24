from tkinter import Tk, Button, Frame, messagebox
import tkinter as tk
from generarNumeros import *
from tkinter import *

generar=generarNumeros()

def ConvR():
    generar.Romanos(varNum.get())

def ConvA():
    generar.Arabigo(int(varNum2.get()))   

ventana=Tk()
ventana.title("Numeros")
ventana.geometry("300x150")

seccion1=Frame(ventana, bg="#ecb5f7")
seccion1.pack(expand=True,fill='both')

varNum=tk.StringVar()
numero=tk.Label(seccion1, text="Ingresa el numero ROMANO que desea convertir: ").pack()
num=tk.Entry(seccion1, width=30, textvariable=varNum).pack()
botonConvertir= Button(seccion1,text="Convertir", bg="#f7b5e3", fg="black", command=ConvR).pack()

varNum2=tk.StringVar()
numero2=tk.Label(seccion1, text="Ingresa el numero ARÁBIGOS que desea convertir: ").pack()
num2=tk.Entry(seccion1, width=30, textvariable=varNum2).pack()
botonConvertir= Button(seccion1,text="Convertir", bg="#f7b5e3", fg="black", command=ConvA).pack()

ventana.mainloop()