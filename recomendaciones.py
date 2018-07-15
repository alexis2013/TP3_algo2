from libreria_grafo import *
from grafo import Grafo


def itinerario(vertices, n_archivo):

	grafo = Grafo(True, False)

	for v in vertices:
		grafo.agregar_vertice(v)

	with open(n_archivo) as archivo:
		linea = archivo.readline()
		linea = linea.rstrip("\n")
		linea = linea.split(",")
		grafo.agregar_arista(linea[0], linea[1])

	return orden_topologico(grafo)

def camino_ini_fin(grafo,desde,hasta):
	
	peso, camino = camino_minimo(grafo,desde,hasta)
	cant_camino = len(camino)
	for i in range(cant_camino-1):
		print("{} -> ".format(camino[i]), end = "")
	print(camino[cant_camino-1])
	print("Costo total: {}".format(peso))
	return camino

def recorrido_optimo(grafo,origen):
	peso, camino = viajante(grafo,origen)
	print (camino)
	print("Costo total: {}".format(peso))
	return camino

def recorrido_aproximado(grafo, origen):

	camino = viajante_aproximado(grafo, origen)
	cant_camino = len(camino)
	for i in range(cant_camino-1):
		print("{} -> ".format(camino[i]), end = "")
	print(camino[cant_camino-1])
	return camino

def reducir_caminos(grafo, n_archivo, ciudades):

	contador = 0
	cant_ciudades = len(ciudades)
	grafo_minimo = arbol_tendido_minimo(grafo)
	with open(n_archivo, "w") as archivo:
		archivo.write("{} \n".format(str(cant_ciudades)))
		for key, values in ciudades.items():
			archivo.write("{},{},{} \n".format(key, *values))
		archivo.write("{} \n".format(str(grafo_minimo.cant_aristas())))
		for v in grafo_minimo.obt_vertices():
			for w in grafo_minimo.obtener_vecinos(v):
				#print(v, " - ", w, " - ", grafo_minimo.ver_peso(v, w))
				contador += grafo_minimo.ver_peso(v, w)
				archivo.write("{},{},{} \n".format(v, w, grafo_minimo.ver_peso(v, w)))
	print(contador)




