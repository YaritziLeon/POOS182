from tkinter import Tk, Button, Frame, messagebox
import random
from tkinter import *
import tkinter as tk
from tkinter import ttk

class generarP13:
        
    def Contraseña(self,lon,mayus,carac):
        
        if (mayus== "no" and carac== "si" and lon >= 8):
            media1="0123456789abcdefghijklmnopqrstuvwxyz<=>@#%&+"
            contra1=[random.choice(media1) for i in range(lon)]
            messagebox.showinfo("Su contraseña no es tan segura: ",contra1)
            ven1=Tk()
            txtContra1=Entry(ven1)
            txtContra1.insert(0,contra1)
            txtContra1.pack()
            ven1.mainloop()
            
        elif (mayus== "si" and carac== "no" and lon >= 8):
            media2="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
            contra2= [random.choice(media2) for i in range(lon)]
            messagebox.showinfo("Su contraseña no es tan segura: ",contra2)
            ven2=Tk()
            txtContra2=Entry(ven2)
            txtContra2.insert(0,contra2)
            txtContra2.pack()
            ven2.mainloop()
            
        elif (mayus== "si" and carac== "si" and lon >= 8):
            segura="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<=>@#%&+"
            contra3= [random.choice(segura) for i in range(lon)]
            messagebox.showinfo("Su contraseña si es segura: ",contra3)
            ven3=Tk()
            txtContra3=Entry(ven3)
            txtContra3.insert(0,contra3)
            txtContra3.pack()
            ven3.mainloop()
            
        elif (mayus == "no" and carac == "no" and lon < 8):
            nsegura="0123456789abcdefghijklmnopqrstuvwxyz"
            contra4= [random.choice(nsegura) for i in range(lon)]
            messagebox.showinfo("Su contraseña no es segura: ",nsegura)
            ven4=Tk()
            txtContra4=Entry(ven4)
            txtContra4.insert(0,contra4)
            txtContra4.pack()
            ven4.mainloop()
        else:
            messagebox.showinfo("Error","La longitud de la contraseña debe igual o mayor a 8")