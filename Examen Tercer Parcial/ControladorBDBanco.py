from tkinter import messagebox
import sqlite3

class controladorBDBanco:
    
    def __init__(self):
        pass
    
    def conexBD(self):
        try:
            conexion=sqlite3.connect("C:/Users/yarit/OneDrive/Documentos/GitHub/POOS182/Examen Tercer Parcial/BD_Banco.db")
            print("Conectado")
            return conexion
        except sqlite3.OperationalError:
            print("No se conecto")
            
    def InsertarCuenta(self,num,sal,nom,cor):
        conex=self.conexBD()
        if(num =="" or sal =="" or nom =="" or cor ==""):
            messagebox.showwarning("Cuidado!!","Formulario incompleto")
            conex.close()
        else:
            cursor1=conex.cursor()
            datos1=(num,sal,nom,cor)
            sqlInsertar="insert into TBCuentas(NoCuenta,Saldo,Nombre,Correo) values(?,?,?,?)"
            cursor1.execute(sqlInsertar,datos1)
            conex.commit()
            conex.close()
            messagebox.showinfo("Correcto","Usuario guardado")