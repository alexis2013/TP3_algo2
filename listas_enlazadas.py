class _Nodo:
    
    def __init__(self, dato=None, prox=None):
        
        self.dato = dato
        
        self.prox = prox
    
    def __str__(self):
        
        return self.dato

class ListaEnlazada:
    
    def __init__(self):
        
        self.prim = None
        
        self.len = 0
        
        self.actual = None
        
    def __str__(self):
        
        resultado = ""
        
        actual_inicial = self.actual
        
        while self.actual :
            
            resultado += self.actual.dato
            
            if not self.actual.prox:
                
                self.actual = actual_inicial
                
                break
            
            resultado += ","
            
            self.next()
            
            
        return resultado
    
    def __len__(self):
        
        return self.len
    
    def append(self, elemento):
        
        self.len += 1
        
        nodo = _Nodo(elemento)
        
        if not self.prim :
            
            self.prim = nodo
            
            self.actual = self.prim
            
            return
            
        actual = self.prim
        
        while actual.prox :
            
            actual = actual.prox
        
        actual.prox = nodo
        
    def next(self):
        
        if not self.actual :
            
            raise StopIteration()
        
        aux = self.actual
        
        self.actual = self.actual.prox
        
        return aux.dato
    
    def extend (self,otro):
        
        if not otro.prim:
            
            return

        if not self.prim:
            
            self.prim = otro.prim
            
            return
        
        actual = self.prim
        
        while actual.prox :
            
            actual = actual.prox
            
        actual.prox = otro.prim
        
    def invertir (self):
        
        if not self.prim:
            
            return
        
        anterior = self.prim
        
        actual = anterior.prox
        
        anterior.prox = None
        
        while actual.prox:
        
            siguiente = actual.prox
            
            actual.prox = anterior
           
            anterior = actual
            
            actual = siguiente
            
        siguiente.prox = anterior
            
        self.prim = siguiente
        
        self.actual = self.prim

    def pop(self, i=None):
        
        """Elimina el nodo de la posición i, y devuelve el dato contenido.
            Si i está fuera de rango, se levanta la excepción IndexError.
            Si no se recibe la posición, devuelve el último elemento."""

        if i is None:
            i = self.len - 1
        if i < 0 or i >= self.len:
            raise IndexError("Índice fuera de rango")
        if i == 0:
            dato = self.prim.dato
            self.prim = self.prim.prox
        else:
            n_ant = self.prim
            n_act = n_ant.prox
        for pos in range(1, i):     
            n_ant = n_act
            n_act = n_ant.prox
            dato = n_act.dato
            n_ant.prox = n_act.prox            
        self.len -= 1        
        return dato
