from libreria_grafo import *
from grafo import Grafo
import sys

def itinerario(vertices, n_archivo):

	grafo = Grafo(True, False)

	for v in vertices:
		grafo.agregar_vertice(v)

	with open(n_archivo) as archivo:
		linea = archivo.readline()
		linea = linea.rstrip("\n")
		linea = linea.split(",")
		grafo.agregar_arista(linea[0], linea[1])

	res = orden_topologico(grafo)
	cant_res = len(res)
	peso = 0
	for i in range(1, cant_res):
		peso += grafo.ver_peso(res[i - 1], res[i])
	stdout_flechas(res, cant_res, peso)
	return res


def camino_ini_fin(grafo, desde, hasta):
	
	camino = camino_minimo(grafo, desde, hasta)
	res, peso = reconstruir_camino(grafo, camino, desde, hasta)
	stdout_flechas(res, len(res), peso)
	return res

def recorrido_optimo(grafo, origen):
	peso, camino = viajante(grafo,origen)
	cant_camino = len(camino)
	stdout_flechas(camino, cant_camino, peso)
	return camino

def recorrido_aproximado(grafo, origen):

	camino, peso = viajante_aproximado(grafo, origen)
	cant_camino = len(camino)
	stdout_flechas(camino, cant_camino, peso)
	return camino

def reducir_caminos(grafo, n_archivo, ciudades):

	contador = 0
	cant_ciudades = len(ciudades)
	grafo_minimo = arbol_tendido_minimo(grafo)
	with open(n_archivo, "w") as archivo:
		archivo.write("{}\n".format(cant_ciudades))
		for key, values in ciudades.items():
			archivo.write("{},{},{}\n".format(key, *values))
		archivo.write("{}\n".format(grafo_minimo.cant_aristas()))
		for v in grafo_minimo.obt_vertices():
			for w in grafo_minimo.obtener_vecinos(v):
				contador += grafo_minimo.ver_peso(v, w)
				archivo.write("{},{},{}\n".format(v, w, grafo_minimo.ver_peso(v, w)))
	return contador

def reconstruir_camino(grafo, diccio, desde, hasta):

	res = []
	aux = hasta
	pila = Pila()
	cont = 0
	peso = 0
	while(aux):
		pila.apilar(aux)
		aux = diccio[aux]
	while(not pila.esta_vacia()):
		res.append(pila.desapilar())
		cont += 1
	for i in range(1, cont):
		peso += grafo.ver_peso(res[i-1], res[i])
	return  res, peso

def stdout_flechas(lista, cant_elem, peso = None):
	for i in range(cant_elem - 1):
		sys.stdout.write("{} -> ".format(lista[i]))
	sys.stdout.write("{}\n".format(lista[cant_elem-1]))
	if peso != None:
		sys.stdout.write("Costo total: {}\n".format(peso))
