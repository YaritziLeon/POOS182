from tkinter import Tk, Button, Frame, messagebox

class generarNumeros:
    
    def Romanos(self,r):
        ro={'I': 1, 'V': 5, 'X': 10, 'L': 50}
        n=0
        for i, j in enumerate(r):
            if(i+1)==len(r) or r[j] >= r[r[i + 1]]:
                n+=ro[j]
            else:
                n-=ro[j]
        roman= arabe(n)
        if roman != r:
            return None
        return n
    messagebox.showinfo("El numero es: ",n)

    def Arabigo(self,a):
        if (a== " " or a>50):
            messagebox.showerror ("Error", "Ingrese un número o un numero menor a 50")
        else:
            x = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
            i = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

            de = x[(a%100)//10]
            uni = i[a%10]
  
            n=(de+uni)
            
            messagebox.showinfo("Conversión exitosa", "El número es: " + n)