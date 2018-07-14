class Heap():

	def __init__(self, cmp):

		self.cmp = cmp
		self.arreglo = []
		self.cantidad = 0

	def esta_vacio(self):

		return self.cantidad == 0

	def obt_cantidad(self):

		return self.cantidad

	def swap(self, pos_a, pos_b):

		aux = self.arreglo[pos_a]
		self.arreglo[pos_a] = self.arreglo[pos_b]
		self.arreglo[pos_b] = aux

	def upheap(self, pos):
		if pos == 0:
			return
		pos_padre = (pos-1) // 2
		if self.cmp(self.arreglo[pos], self.arreglo[pos_padre]) > 0:
			return
		self.swap(pos, pos_padre)
		return self.upheap(pos_padre)

	def downheap(self, pos):
		if pos >= self.cantidad:
			return
		pos_hijo_1 = pos * 2 + 1
		pos_hijo_2 = pos * 2 + 2
		if pos_hijo_1 >= self.obt_cantidad():
			return
		if pos_hijo_2 >= self.obt_cantidad():
			a_comparar = pos_hijo_1
		else:
			res_cmp = self.cmp(self.arreglo[pos_hijo_1], self.arreglo[pos_hijo_2])
			if res_cmp < 0:
				a_comparar = pos_hijo_1
			else:
				a_comparar = pos_hijo_2
		if self.cmp(self.arreglo[a_comparar], self.arreglo[pos]) > 0:
			return
		self.swap(a_comparar, pos)
		return self.downheap(a_comparar)

	def encolar(self, elemento):

		self.arreglo.append(elemento)
		self.cantidad += 1
		if self.cantidad >= 2 :
			self.upheap(self.obt_cantidad() -1)

	def desencolar(self):

		if(self.esta_vacio()):
			return None
		self.swap(0, self.obt_cantidad() -1)
		res = self.arreglo.pop()
		self.cantidad -= 1
		self.downheap(0)
		return res

	def obt_arreglo(self):

		return self.arreglo


