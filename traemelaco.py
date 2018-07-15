from math import inf
from grafo import Grafo
from cola import Cola
from pila import Pila
from heap_reducido import Heap
from libreria_grafo import *
from wrapper_comandos import *
from manejo_kml import *
import sys
import ctypes, ctypes.util

def joinear_ciudades(cadenas):
	
	i = 0
	cant_cadenas = len(cadenas)
	while i < cant_cadenas:
		if cadenas[i][-1] == ",":
			cadenas[i] = cadenas[i].rstrip(",")
		if cadenas[i] not in diccionario_ciudades:
			cadenas[i] = " ".join(cadenas[i : i + 2])
			cant_cadenas -= 1
		i += 1
	return cadenas

if len(sys.argv) != 3:
	print("error cantidad argumentos invalida \n")

grafo = Grafo(False,True)
diccionario_ciudades = {}

with open(sys.argv[2], "w") as archivo:
	archivo.write('<?xml version="1.0" encoding="UTF-8"?>\n')
	archivo.write('<kml xmlns="http://earth.google.com/kml/2.1">\n')
	archivo.write("\t<Document>\n")

with open(sys.argv[1], "r") as archivo:
	
	linea = archivo.readline()
	linea = linea.rstrip("\n")
	
	while linea:
		cant_ciudades = int(linea)
		for i in range(cant_ciudades):
			linea = archivo.readline()
			linea = linea.rstrip("\n")
			linea = linea.split(",")
			grafo.agregar_vertice(linea[0])
			diccionario_ciudades[linea[0]] = [linea[1], linea[2]]
		linea = archivo.readline()
		linea = linea.rstrip("\n")
		cant_aristas = int(linea)
		for i in range(cant_aristas):
			linea = archivo.readline()
			linea = linea.rstrip("\n")
			linea = linea.split(",")
			grafo.agregar_arista(linea[0], linea[1], int(linea[2]))
		linea = archivo.readline()
		linea = linea.rstrip("\n")

for linea in sys.stdin:
	linea = linea.rstrip("\n")
	cadenas = linea.split(" ")

	if(cadenas[0] == "ir"):
		cadenas[1:] = joinear_ciudades(cadenas[1:])
		resul = camino_ini_fin(grafo, cadenas[1], cadenas[2])
		escribir_kml(sys.argv[2], resul, diccionario_ciudades, linea)

	elif(cadenas[0] == "viaje"):
		cadenas[2:] = joinear_ciudades(cadenas[2:])
		if cadenas[1] == "aproximado," : 
			resul = recorrido_aproximado(grafo, cadenas[2])
			escribir_kml(sys.argv[2], resul, diccionario_ciudades, linea)
		elif(cadenas[1] == "optimo,"):
			resul = recorrido_optimo(grafo, cadenas[2])
			escribir_kml(sys.argv[2], resul, diccionario_ciudades, linea)
		
	elif(cadenas[0] == "itinerario"):
		cadenas[1:] =  joinear_ciudades(cadenas[1:])
		res = itinerario(grafo.obt_vertices(), cadenas[1])
		escribir_kml(sys.argv[2], res, diccionario_ciudades, linea)

	elif(cadenas[0] == "reducir_caminos"):
		res = reducir_caminos(grafo, cadenas[1], diccionario_ciudades)
		sys.stdout.write("Peso total: {}\n".format(res))

with open(sys.argv[2], "a+") as archivo:
	archivo.write("\t</Document>\n")
	archivo.write("</kml>\n")