class nodo:
    def __init__(self,cedula,nombre,hab):
        self.cedula = cedula
        self.nombre = nombre
        self.hab = hab
        self.siguiente = None

class libro:
    def __init__(self):
        self.cabeza = None
        self.tamaño = 1
    
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
        self.libro_entradas = libro()
        self.libro_salidas = libro()
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
            self.libro_salidas.insertar(self.cabeza.cedula,self.cabeza.nombre,self.cabeza.hab)
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
                self.libro_salidas.insertar(recorre.cedula,recorre.nombre,recorre.hab)
                recorre.siguiente = recorre.siguiente.siguiente
                self.n0_hab += 1
            else:
                print("Posicion no encontrada")
    
    def imprimir_actuales(self):
        recorre = self.cabeza
        print("----------Huespedes Actuales----------")
        while(recorre):
            print("\nNombre:",recorre.nombre)
            print("Cédula:",recorre.cedula)
            print("Número de habitación:",recorre.hab)
            recorre = recorre.siguiente
    
    def imprimir_libro_entradas(self):
        recorre = self.libro_entradas.cabeza
        print("--------------------Libro de entradas--------------------")
        while(recorre):
            print("\nIngreso #", self.libro_entradas.tamaño)
            print("Nombre:",recorre.nombre)
            print("Cédula:",recorre.cedula)
            print("Habitación:",recorre.hab)
            self.libro_entradas.tamaño += 1
            recorre = recorre.siguiente

    def imprimir_libro_salidas(self):
        recorre = self.libro_salidas.cabeza
        print("--------------------Libro de salidas--------------------")
        while(recorre):
            print("\nSalida #", self.libro_salidas.tamaño)
            print("Nombre:",recorre.nombre)
            print("Cédula:",recorre.cedula)
            print("Habitación:",recorre.hab)
            self.libro_salidas.tamaño += 1
            recorre = recorre.siguiente

    def consulta_huespedes(self):
        c = int(input("Ingrese el tipo de consulta:\n 1.Indivual \n 2.Total \n"))
        if(c == 1):
            ced = input("Ingrese el documento del huesped: \n")
            recorre = self.libro_entradas.cabeza
            recorre_2 = self.libro_salidas.cabeza
            while(ced != recorre_2.cedula and recorre_2.siguiente != None):
                self.libro_salidas.tamaño += 1
                recorre_2 = recorre_2.siguiente
            if(ced == recorre_2.cedula):    
                while(ced != recorre.cedula and recorre):
                    self.libro_entradas.tamaño += 1
                    recorre = recorre.siguiente
                print("----------Datos huesped----------")
                print("\nNombre:",recorre.nombre)
                print("Cédula:",recorre.cedula)
                print("Habitación:",recorre.hab)
                print("Número de ingreso:",self.libro_entradas.tamaño)
                print("Número de salida:",self.libro_salidas.tamaño)
            else:
                while(ced != recorre.cedula and recorre):
                    self.libro_entradas.tamaño += 1
                    recorre = recorre.siguiente
                print("----------Datos huesped----------")
                print("\nNombre:",recorre.nombre)
                print("Cédula:",recorre.cedula)
                print("Habitación:",recorre.hab)
                print("Número de ingreso:",self.libro_entradas.tamaño)
                print("El huesped aún sigue ocupando la habitación.")
        elif(c == 2):
            self.imprimir_libro_entradas()

    def consulta_habitaciones(self):
        print("Habitaciones disponibles:",self.n0_hab,"/ 100")

huespedes = lista()

huespedes.insertar("1095843221","Cristian Alvarez",10)
huespedes.insertar("1095849121","Laura Garcia",6)
huespedes.insertar("113843721","Andrea Bernal",4)
huespedes.insertar("323843221","Martin Morales",18)
huespedes.insertar("113848821","Kevin Almiron",3)
huespedes.insertar("112943221","Carlos Lozano",5)
huespedes.insertar("114863221","Maxi Lozano",10)
huespedes.insertar("100843571","Sebastian Lozano",14)
huespedes.insertar("109843221","Miguel Angulo",16)

huespedes.eliminar(0)
huespedes.eliminar(7)

huespedes.consulta_huespedes()