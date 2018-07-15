import math

class Grafo:

	def __init__(self, dirigido = False, pesado = False):

		self.grafo = {}
		self.es_dirigido = dirigido
		self.pesado = pesado
		self.cantidad_vertices = 0
		self.cantidad_aristas = 0
		self.vertices = []

	def vertice_esta(self, vertice):

		return vertice in self.grafo

	def es_pesado(self):

		return self.pesado

	def es_dirigido(self):

		return self.es_dirigido

	def agregar_vertice(self, vertice):

		self.grafo[vertice] = {}
		self.vertices.append(vertice)
		self.cantidad_vertices += 1
		return True

	def borrar_vertice(self, vertice):

		if not self.vertice_esta(vertice):
			return None
		self.cantidad -= 1
		self.vertice.remove(vertice)
		return self.grafo.pop(vertice)

	def agregar_arista(self, desde, hasta, peso = None):

		if not self.vertice_esta(desde) and not self.vertice_esta(hasta):
			return False

		self.grafo[desde][hasta] = peso
		if not self.es_dirigido:
			self.grafo[hasta][desde] = peso
			self.cantidad_aristas += 1
		self.cantidad_aristas += 1
		return True

	def borrar_arista(self, desde, hasta):
		if not self.vertice_esta(desde) and not self.vertice_esta(hasta):
			return False
		self.grafo[desde].pop(hasta)
		if not self.es_dirigido:
			self.grafo[hasta].pop(desde)
			self.cantidad_aristas -= 1
		self.cantidad_aristas -= 1
		return True

	def ver_peso(self, desde, hasta):
		if not self.es_pesado:
			return 1
		return self.grafo[desde][hasta]

	def obt_vertices(self):

		return self.vertices

	def obt_1_vertice(self):

		return self.obt_vertices()[0]

	def obtener_vecinos(self, vertice):

		if not self.vertice_esta(vertice):
			return []
		res = []
		for v in self.grafo[vertice].keys():
			res.append(v)
		return res

	def cant_vertices(self):

		return self.cantidad_vertices

	def cant_aristas(self):

		return self.cantidad_aristas

