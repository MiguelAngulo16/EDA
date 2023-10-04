class nodo:
    def __init__(self,cedula,nombre,hab):
        self.cedula = cedula
        self.nombre = nombre
        self.hab = hab
        self.siguiente = None

class lista:
    def __init__(self):
        self.cabeza = None
        self.tamano = 0

    def listaVacia(self):
        if self.cabeza == None:
            return True
        else:
            return False
    def insertarFinal(self, cedula, nombre, hab):
        nodo_nuevo = nodo(cedula,nombre,hab)
        recorre = self.cabeza
        if(self.listaVacia()):
            nodo_nuevo = nodo(cedula, nombre, hab)
            nodo_nuevo.siguiente = self.cabeza
            self.cabeza = nodo_nuevo
            self.tamano = self.tamano + 1
        else:
            while (recorre.siguiente != None):
                recorre = recorre.siguiente
            recorre.siguiente = nodo_nuevo
            self.tamano = self.tamano + 1
                
    def eliminarInicio(self):
        if(self.listaVacia()):
            print("La lista está vacia")
        else:
            self.cabeza = self.cabeza.siguiente
            self.tamano = self.tamano - 1
            
    def eliminar_idx(self,idx):
        if(self.listaVacia()):
            pass
        
        recorre = self.cabeza
        pos = 0
        if(pos == idx):
            self.eliminarInicio()
        else:
            while(recorre != None and (pos+1) != idx):
                pos += 1
                recorre = recorre.siguiente
                
            if recorre != None:
                recorre.siguiente = recorre.siguiente.siguiente
            else:
                print("Posicion no encontrada")
    
    def imprimir_lista(self):
        recorre = self.cabeza
        cont = 1
        while(recorre):
            print("\nIngreso #",cont)
            print("Nombre:",recorre.nombre)
            print("Cédula:",recorre.cedula)
            print("Habitación:",recorre.hab)
            recorre = recorre.siguiente
            cont += 1


huespedes = lista()

huespedes.insertarFinal("1095843221","Cristian Alvarez",10)
huespedes.insertarFinal("1095849121","Laura Garcia",6)
huespedes.insertarFinal("113843221","Kevin Lozano",3)
huespedes.insertarFinal("113843221","Kevin Lozano",3)
huespedes.insertarFinal("113843221","Kevin Lozano",3)
huespedes.insertarFinal("113843221","Kevin Lozano",3)
huespedes.insertarFinal("113843221","Kevin Lozano",3)
huespedes.insertarFinal("113843221","Kevin Lozano",3)
huespedes.insertarFinal("113843221","Kevin Lozano",3)

huespedes.eliminar_idx(1)
huespedes.eliminar_idx(4)
huespedes.eliminar_idx(7)


