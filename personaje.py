class Personaje:
    #atributos
    especie="Hunamano"
    nombre="MasterChief"
    altura=2.70
    
    #metodos
    def correr(self,status):
        if(status):
            print("El personaje "+self.nombre+"esta corriendo")
        else:
            print("El personaje "+self.nombre+"se detuvo")