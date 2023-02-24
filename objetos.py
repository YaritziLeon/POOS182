from personaje import *

#1. Solicitamos los datos
print("")
print("DATOS HEROE: ")
especieH=input("Escribe la especie del Heroe: ")
nombreH=input("Escribe el nombre del Heroe: ")
alturaH=float(input("Escribe la altura del Heroe: "))
recargaH=int(input("Ingresa las balas para el Heroe: "))

print("")
print("DATOS VILLANO: ")
especieV=input("Escribe la especie del Villano: ")
nombreV=input("Escribe el nombre del Villano: ")
alturaV=float(input("Escribe la altura del Villano: "))
recargaV=int(input("Ingresa las balas para el Villano: "))

#2. Creamos los objetos
Heroe=Personaje(especieH, nombreH, alturaH)
Villano=Personaje(especieV, nombreV, alturaV)

Heroe.setNombre("pepe")

#3. usamos los atributos Heroe y Villano

print("")
print("Metodos y Atributos del Heroe: ")
print("El personaje se llama: "+Heroe.getNombre())
print("Pertenece a la especie: "+Heroe.getEspecie())
print("Y una altura de: "+str(Heroe.getAltura()))

Heroe.correr(True)
Heroe.lanzarGranadas()
Heroe.recargarArma(37)

print("")
print("Metodos y Atributos del VILLANO: ")
print("El personaje se llama: "+Villano.getNombre())
print("Pertenece a la especie: "+Villano.getEspecie())
print("Y una altura de: "+str(Villano.getAltura()))

Villano.correr(True)
Villano.lanzarGranadas()
Villano.recargarArma(37)
#Villano.__pensar()