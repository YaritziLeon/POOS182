class Personaje:
    #atributos
    especie="Hunamano"
    nombre="MasterChief"
    altura=2.70
    
    #metodos
    def correr(self,status):
        if(status):
            print("El personaje "+self.nombre+" esta corriendo")
        else:
            print("El personaje "+self.nombre+" se detuvo")

    def lanzarGranadas(self):
        print("El personaje "+self.nombre+" lanzo granada")
    
    def recargarArma(self,municiones):
        cargador=10
        cargador=cargador+municiones
        print("El arma recargada tiene "+cargador+" balas")