class nodo:
    def __init__(self,cedula,nombre,hab):
        self.cedula = cedula
        self.nombre = nombre
        self.hab = hab
        self.siguiente = None

class libro_entrada:
    def __init__(self):
        self.cabeza = None
        self.no_ingreso = 1
    
    def listaVacia(self):
        if self.cabeza == None:
            return True
        else:
            return False

    def insertar(self, cedula, nombre, hab):
        nodo_nuevo = nodo(cedula,nombre,hab)
        recorre = self.cabeza
        if(self.listaVacia()):
            nodo_nuevo = nodo(cedula, nombre, hab)
            nodo_nuevo.siguiente = self.cabeza
            self.cabeza = nodo_nuevo
        else:
            while (recorre.siguiente != None):
                recorre = recorre.siguiente
            recorre.siguiente = nodo_nuevo

class lista:
    def __init__(self):
        self.cabeza = None
        self.libro_entradas = libro_entrada()
        self.n0_hab = 100

    def listaVacia(self):
        if self.cabeza == None:
            return True
        else:
            return False
        
    def insertar(self, cedula, nombre, hab):
        nodo_nuevo = nodo(cedula,nombre,hab)
        recorre = self.cabeza
        if(self.listaVacia()):
            nodo_nuevo = nodo(cedula, nombre, hab)
            nodo_nuevo.siguiente = self.cabeza
            self.cabeza = nodo_nuevo
            self.n0_hab -= 1
            self.libro_entradas.insertar(cedula,nombre,hab)
        else:
            while (recorre.siguiente != None):
                recorre = recorre.siguiente
            recorre.siguiente = nodo_nuevo
            self.n0_hab -= 1
            self.libro_entradas.insertar(cedula,nombre,hab)
                       
    def eliminarInicio(self):
        if(self.listaVacia()):
            print("Todas las habitaciones estan disponibles.")
        else:
            self.cabeza = self.cabeza.siguiente
            self.n0_hab += 1
            
    def eliminar(self,idx):
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
                self.n0_hab += 1
            else:
                print("Posicion no encontrada")

    def consulta_huespedes(self):
        c = int(input("Ingrese el tipo de consulta:\n 1.Indivual \n 2.Total \n"))
        if(c == 1):
            ced = input("Ingrese el documento del huesped: \n")
            recorre = self.libro_entradas.cabeza
            recorre_2 = self.cabeza
            while(ced != recorre.cedula and (recorre and recorre_2)):
                recorre = recorre.siguiente
                recorre_2 = recorre_2.siguiente
                self.libro_entradas.no_ingreso += 1
            if(ced == recorre.cedula):
                print("\nNombre:",recorre.nombre)
                print("Cédula:",recorre.cedula)
                print("Habitación:",recorre.hab)
                print("No. de ingreso:",self.libro_entradas.no_ingreso)
        elif(c == 2):
            recorre = self.libro_entradas.cabeza
            while(recorre):
                print("\nIngreso #", self.libro_entradas.no_ingreso)
                print("Nombre:",recorre.nombre)
                print("Cédula:",recorre.cedula)
                print("Habitación:",recorre.hab)
                self.libro_entradas.no_ingreso += 1
                recorre = recorre.siguiente

huespedes = lista()

huespedes.insertar("1095843221","Cristian Alvarez",10)
huespedes.insertar("1095849121","Laura Garcia",6)
huespedes.insertar("113843221","Kevin Lozano",3)
huespedes.insertar("113843221","Kevin Lozano",3)
huespedes.insertar("113843221","Kevin Lozano",3)
huespedes.insertar("113843221","Carlos Lozano",3)
huespedes.insertar("113843221","Maxi Lozano",3)
huespedes.insertar("113843571","Sebastian Lozano",14)
huespedes.insertar("109843221","Juan Lozano",3)

huespedes.eliminar(2)
huespedes.eliminar(7)

huespedes.consulta_huespedes()