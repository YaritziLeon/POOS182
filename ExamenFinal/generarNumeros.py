from tkinter import Tk, Button, Frame, messagebox

class generarNumeros:
    
    def __init__(self):
        self.romanos={'I':1,'II':2,'III':3,'IV':4,'V':5,'VI':6,'VII':7,'VIII':8,'IX':9,'X':10,'XI':11,
                                 'XII':12,'XIII':13,'XIV':14,'XV':15,'XVI':16,'XVII':17,'XVIII':18,'XIX':19,'XX':20,
                                 'XXI':21,'XXII':22,'XXIII':23,'XXIV':24,'XXV':25,'XXVI':26,'XXVII':27,'XXVIII':28,
                                 'XXIX':29,'XXX':30,'XXXI':31,'XXXII':32,'XXXIII':33,'XXXIV':34,'XXXV':35,'XXXVI':36,
                                 'XXXVII':37,'XXXVIII':38,'XXXIX':39,'XL':40,'XLI':41,'XLII':42,'XLIII':43,'XLIV':44,
                                 'XLV':45,'XLVI':46,'XLVII':47,'XLVIII':48,'XLIX':49,'L':50}
    def Romanos(self,numero):
        
        if (numero not in self.romanos):
            messagebox.showinfo("ERROR","El número es invalido")
        else:
            resul=0
            i=0
            while i < len(numero):
                if i + 1 < len(numero) and self.romanos[numero[i]] < self.romanos[numero[i + 1]]:
                    resul += self.romanos[numero[i + 1]] - self.romanos[numero[i]]
                    i+=2
                else:
                    resul += self.romanos[numero[i]]
                    i+=1
            messagebox.showinfo("El numero es: ",resul)

    
    def Arabigo(self,a):
        if (a>50):
            messagebox.showerror ("Error", "Ingrese un número menor a 50")
        else:
            x = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
            i = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

            de = x[(a%100)//10]
            uni = i[a%10]
  
            n=(de+uni)
            
            messagebox.showinfo("Conversión exitosa", "El número es: " + n)