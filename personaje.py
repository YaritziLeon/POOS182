class Personaje:
    
    #Agregamos el constructor del personaje
    def __init__(self,esp,nom,alt):
    #atributos
        self.especie=esp
        self.nombre=nom
        self.altura=alt
    
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
        print("El arma recargada tiene "+str(cargador)+" balas")