from listas_enlazadas import ListaEnlazada

class Pila:
    
    def __init__(self):
        
        self.items = []
        
    def esta_vacia(self):
        
        """Devuelve True si la lista está vacía, False si no."""

        return len(self.items) == 0
    
    def apilar(self, x):
        
        """Apila el elemento x."""
        
        self.items.append(x)
        
    def desapilar(self):
        
        if self.esta_vacia():
            
            raise ValueError("vacia")
        
        return self.items.pop()
    
    def ver_tope(self):
        
        if self.esta_vacia():
            
            raise ValueError()
        
        return self.items[-1]


