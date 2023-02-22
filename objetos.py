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

#3. usamos los atributos Heroe y Villano

print("")
print("Metodos y Atributos del Heroe: ")
print("El personaje se llama: "+Heroe.nombre)
print("Pertenece a la especie: "+Heroe.especie)
print("Y una altura de: "+str(Heroe.altura))

Heroe.correr(True)
Heroe.lanzarGranadas()
Heroe.recargarArma(37)

print("")
print("Metodos y Atributos del VILLANO: ")
print("El personaje se llama: "+Villano.nombre)
print("Pertenece a la especie: "+Villano.especie)
print("Y una altura de: "+str(Villano.altura))

Villano.correr(True)
Villano.lanzarGranadas()
Villano.recargarArma(37)
