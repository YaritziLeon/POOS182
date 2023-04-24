from tkinter import messagebox

class generarP14:
    
    def __init__(self):
        self.__saldo=1000    
        

    def Consultar(self):
        return self.__saldo
        
        
    def Ingresar(self,sa):
        saldo=self.__saldo+sa
        messagebox.showinfo("El saldo es: ",str(saldo))
        self.__saldo=saldo

    def Retirar(self,sa):
        if(sa<=self.__saldo):
            saldo=self.__saldo-sa
            messagebox.showinfo("El saldo es: ",str(saldo))
            self.__saldo=saldo
        else:
            messagebox.showinfo("Error","Saldo insuficiente")
    
    def Depositar(self,sa):
        if(sa<=self.__saldo):
            saldo=self.__saldo-sa
            messagebox.showinfo("El saldo restante es: ",str(saldo))
            self.__saldo=saldo
        else:
            messagebox.showinfo("Error","Saldo insuficiente")
    
    
    def getSaldo(self):
        return self.__saldo
    def setSaldo(self,s):
        self.__saldo=s