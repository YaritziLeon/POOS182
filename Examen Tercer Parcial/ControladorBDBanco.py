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
            
    
    def actualizarCuenta(self,num2,sal2,nom2,cor2,id):
        
        conex=self.conexionBD()
        if(num2 =="" or sal2 =="" or nom2 =="" or cor2 =="" or id ==""):
            messagebox.showwarning("Error","Llena el Formulario")
            conex.close()
        else:
            try:
                cursor2=conex.cursor()
                
                sqlActualizar="update TBCuentas set NoCuenta=?,Saldo=?,Nombre=?,Correo=? where IDCuenta= "+id
                datos2=(num2,sal2,nom2,cor2)
                cursor2.execute(sqlActualizar,datos2)
                conex.commit()
                conex.close()
            except sqlite3.OperationalError:
                print("Error")
    
    
    def consultarCuentas(self):
        conex=self.conexBD()
        try:
            cursor3=conex.cursor()
            sqlConsultar="select * from TBCuentas"
            cursor3.execute(sqlConsultar)
            Con=cursor3.fetchall()
            conex.close()
            return Con
        except sqlite3.OperationalError:
            print("Error")