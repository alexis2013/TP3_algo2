from math import inf
from grafo import Grafo
from cola import Cola
from pila import Pila
from heap_reducido import Heap

def cmp_arista(a_1, a_2):
	if a_1[2] > a_2[2]:
		return 1
	if a_1[2] < a_2[2]:
		return -1
	return 0


def dijkstra(grafo, inicio,fin):

	heap = Heap(cmp_arista)
	pesos = {}

	for v in grafo.obt_vertices():
		pesos[v] = inf
	padres = {inicio : None}
	pesos[inicio] = 0

	heap.encolar((None,inicio,pesos[inicio]))

	while(not heap.esta_vacio()):
		arista = heap.desencolar()
		hasta = arista[1]
		desde = arista[0]
		if(desde == fin):      
			return pesos, padres

		for v in grafo.obtener_vecinos(hasta):
			if pesos[v] > pesos[hasta] + int(grafo.ver_peso(hasta,v)):
				padres[v] = hasta
				pesos[v] = pesos[hasta] + int(grafo.ver_peso(hasta,v))
				heap.encolar((hasta, v, int(pesos[v])))
	return padres			


def bfs(grafo, inicio):

	if not grafo.vertice_esta(inicio):
		return None
	cola = Cola()
	visitados = set()
	padres = {}
	padres[inicio] = None
	visitados.add(inicio)
	cola.encolar(inicio)
	while(not cola.esta_vacia()):
		vertice = cola.desencolar()
		for v in grafo.obtener_vecinos(vertice):
			if v in visitados:
				continue
			visitados.add(v)
			padres[v] = vertice
			cola.encolar(v)
	return padres

def camino_minimo(grafo, desde, hasta):

	res = []
	if grafo.es_pesado():
		caminos = dijkstra(grafo, desde, hasta)
	else:
		caminos = bfs(grafo, desde)
	return caminos


def minimo_viajante (camino , peso , camino2, peso2):
	if (peso > peso2):
		return True
	return False

def _dfs_viajante(grafo,origen,v,peso_final,peso_actual,camino_actual,camino_final,visitados,peso_arista):
	
	camino_actual.append(v)
	
	visitados.add(v)
	if peso_actual > peso_final:
		return camino_final, peso_final

	if (len(camino_final) == len(camino_actual)):
		if minimo_viajante(camino_final, peso_final, camino_actual, peso_actual+grafo.ver_peso(origen,v)):
			camino_final = camino_actual.copy()
			peso_final = peso_actual + grafo.ver_peso(origen,v)
			print(camino_final)
			print(peso_final)
		return camino_final, peso_final

	for w in grafo.obtener_vecinos(v):
		if w in visitados:
			continue
		peso_arista = grafo.ver_peso(v,w)
		peso_actual+= peso_arista
		camino_final, peso_final = _dfs_viajante(grafo,origen,w,peso_final,peso_actual,camino_actual,camino_final,visitados,peso_arista)
		visitados.remove(w)
		peso_actual -= peso_arista
		camino_actual.remove(w)
	return camino_final , peso_final
	
def viajante(grafo, origen):   #solo para no dirigido, pesado, y completo
	if not grafo.vertice_esta(origen):
		return None	

	visitados = set()
	restantes = set()
	camino = []
	visitados.add(origen)
	camino.append(origen)
	peso = 0
	anterior = origen
	for v in grafo.obt_vertices():
		if v in visitados:
			continue
		camino.append(v)
		peso = float(grafo.ver_peso(anterior , v)) + peso
		anterior = v
	peso += float(grafo.ver_peso(anterior, origen))
	camino, peso = _dfs_viajante(grafo,origen,origen, peso, 0, [], camino,set(),0)
	camino.append(origen)
	return peso, camino

def viajante_aproximado(grafo, origen):

	if not grafo.vertice_esta(origen):
		return None	
	camino = []
	visitados = set()
	ultimo = origen
	while ultimo:
		visitados.add(ultimo)
		camino.append(ultimo)
		heap = Heap(cmp_arista)
		for v in grafo.obtener_vecinos(ultimo):
			if v in visitados:
				continue
			heap.encolar((ultimo,v,grafo.ver_peso(ultimo,v)))
		if heap.esta_vacio():
			ultimo = None
		else:
			arista = heap.desencolar()
			ultimo = arista[1]
	camino.append(origen)
	return camino

def orden_topologico(grafo):

	res = []
	orden = {}
	visitados = set()
	for v in grafo.obt_vertices():
		orden[v] = 0
	for v in grafo.obt_vertices():
		for w in grafo.obtener_vecinos(v):
			orden[w] += 1
	cola = Cola()
	for v, grado in orden.items():
		if grado == 0:
			cola.encolar(v)
	while(not cola.esta_vacia()):
		v = cola.desencolar()
		if v in visitados:
			continue
		res.append(v)
		visitados.add(v)
		for w in grafo.obtener_vecinos(v):
			orden[w] -= 1
		for v, grado in orden.items():
			if grado == 0 :
				cola.encolar(v)
	return res

def arbol_tendido_minimo(grafo):  #mst_prim
	inicio = grafo.obt_1_vertice()
	visitados = set()
	visitados.add(inicio)
	heap = Heap(cmp_arista)
	arbol = Grafo(True, True)
	for v in grafo.obt_vertices():
		arbol.agregar_vertice(v)
	for v in grafo.obtener_vecinos(inicio):
		heap.encolar((inicio, v, grafo.ver_peso(inicio, v)))
	while not heap.esta_vacio():
		arista = heap.desencolar()
		v = arista[1]
		if v in visitados:
			continue
		arbol.agregar_arista(arista[0], arista[1], arista[2])
		visitados.add(v)
		for w in grafo.obtener_vecinos(v):
			heap.encolar((v ,w , grafo.ver_peso(v,w)))
	return arbol