class nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class listaCircularDoble():
    def __init__(self):
        self.cabeza = None
        self.ultimo = None

    def listaVacia(self):
        if (self.cabeza == None):
            return True
        else:
            return False
    
    def insertarInicio(self,dato):
        nuevo = nodo(dato)
        if(self.listaVacia()):
            self.cabeza = nuevo
            self.cabeza = self.ultimo
        else:
            nuevo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo
            self.cabeza = nuevo
            self.cabeza.anterior = self.ultimo
            self.ultimo.siguiente = self.cabeza
    
    def insertarFinal(self,dato):
        nuevo = nodo(dato)
        if(self.listaVacia()):
            self.insertarInicio(dato)
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = nuevo
            self.ultimo.anterior = aux
            self.cabeza.anterior = self.ultimo
            self.ultimo.siguiente = self.cabeza
    
    def imprimir_inicio(self):
        recorre = self.cabeza
        while(recorre):
            print(recorre.dato)
            recorre = recorre.siguiente
            if(recorre == self.cabeza):
                break
