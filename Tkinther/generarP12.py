from tkinter import messagebox

class generarP12:
    
    def __init__ (self):
        self.__contraC="leonmontero2003"
        self.__correoC="yaritzileonm08@gmail.com"
    
    
        
    def Comprobar(self, correo, contra):
        if (correo == "" or contra == ""):
            messagebox.showerror('Error', "Llene todo lo que se le solicita")
        else:
            if (self.__correoC==correo and  self.__contraC==contra):
                messagebox.showinfo('Completado', "Se inicio sesion de manera correcta")
            else:
                messagebox.showerror('Error', "Contraseña incorrecta")