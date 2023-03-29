from tkinter import messagebox
import sqlite3
import bcrypt

class controladorBD:
    
    def __init__(self):
        pass
    
    def conexionBD(self):
        #va a intentar algo
        try:
            conexion=sqlite3.connect("C:/Users/yarit/OneDrive/Documentos/GitHub/POOS182/tkinterSQLite/DBUsuarios.db")
            print("Conectado a la BD")
            return conexion
        except sqlite3.OperationalError:
            print("No se pudo conectar ")
        
    def guardarUsuario(self,nom,cor,con):
        #1. Mandar llamar el metodo conexion--- mandar llamar mi propio metodo en una clase
        conex=self.conexionBD()
        #Validor vacios 
        if(nom =="" or cor =="" or con ==""):
            messagebox.showwarning("Cuidado!!","Formulario incompleto")
            conex.close()
        else:
            #cuando los datos no esten vacios vamoa hacer lo soguiente:
            #3.Realiar el insert a la BD--- cremos un objeto llamado cursor con la conexion
            #Preparamos las variables necesarias
            cursor=conex.cursor()
            conH=self.encriptarContra(con)
            #Preparar los datos dentro de una lista
            datos=(nom,cor,conH)
            #crear una variable para hacer la insersion
            sqlInsert="insert into tbregistrados(nombre,correo,contra) values(?,?,?)"
                
            #5.Ejecutamos inserts y cerramos la conexion
            cursor.execute(sqlInsert,datos)
            conex.commit()
            conex.close()
            messagebox.showinfo("Correcto","Usuario guardado")
                
    def encriptarContra(self,con):
        #Preparamos la contraseña y la sal  para Hash
        conPlana=con
        #Convertir a bytes
        conPlana=conPlana.encode()  
        sal=bcrypt.gensalt()
        #Encriptamos
        conHa=bcrypt.hashpw(conPlana,sal)
        print(conHa)
        #regresamos la contraseña encriptada
        return conHa
    
    def consultarUsuario(self,id):
        #1.Realizar conexion BD
        conex=self.conexionBD()
        #2.Verificar el ID
        if(id==""):
            messagebox.showwarning("Cuidado","Escribe un Identificador")
            conex.close()
        else:
            #3.Proceder a la consulta
            try:
                #4.Preparamos lo necesario
                cursor=conex.cursor()
                sqlSelect="select * from tbregistrados where id= "+id
                #5.Ejecutamos y cerramos conexion
                cursor.execute(sqlSelect)
                #fetchall toma todo y lo pasa a una variable 
                RSusuario=cursor.fetchall()
                conex.close()
                return RSusuario
            except sqlite3.OperationalError:
                print("Error de consulta")