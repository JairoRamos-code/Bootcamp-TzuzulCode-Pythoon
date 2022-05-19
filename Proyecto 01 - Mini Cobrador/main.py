class MiniCobrador:

    def __init__(self):
        # [NombreDelProducto, Precio, StockDisponible]
        self.stockTotal = [["Pinza Fuerza", 700, 5],
                        ["Pinza Punta", 750, 8],
                        ["Taladro", 2500, 6],
                        ["Destornillador", 450, 7]]
        self.carritoCliente = []

    # Opción 1. Muestra la lista de productos en stock
    def listaDeProductos(self):
        print (f"\nLista de productos: NombreDelProducto | Precio x Unidad | Stock Disponible")
        i = 0
        while i < len(self.stockTotal):
            print (f"ID:[{i}] {self.stockTotal[i][0]} | ${self.stockTotal[i][1]} | {self.stockTotal[i][2]} unidades disponibles")
            i += 1

    # Opción 2.
    def agregarProductoAlStock(self):
        pass

    # Opción 3.
    def removerProductoDelStock(self, idProducto, unidadesSolicitadas):
        self.stockTotal[idProducto][2] = self.stockTotal[idProducto][2] - unidadesSolicitadas
        return self.stockTotal[idProducto][2]

    # Opción 4. Agregar productos al carrito del cliente. Usa varias funciones auxiliares.
    def anadirACarritoCliente(self):
        try: # ¿El ID está compuesto solo por números?
            idProducto = int(input("\nElija el ID del producto: "))
            if idProducto >= 0 and idProducto < len(self.stockTotal): # ¿El ID está en el rango adecuado?
                if self.mostrarStockDelProducto(idProducto) > 0: # ¿Hay stock del producto?
                    try: # ¿Se solicita una cantidad numérica valida?
                        unidadesSolicitadas = int(input("\nElija la cantidad de unidades: "))
                        if unidadesSolicitadas >= 1 and unidadesSolicitadas <= self.stockTotal[idProducto][2]:
                            precioProducto = self.calcularPrecioProducto(idProducto, unidadesSolicitadas)
                            nombreProducto = self.obtenerNombreProducto(idProducto)
                            self.carritoCliente.append([nombreProducto, precioProducto]) # se implementa con listas
                            self.removerProductoDelStock(idProducto, unidadesSolicitadas)
                        else:
                            print(f"*** {unidadesSolicitadas} es una cantidad errónea. Hay {self.mostrarStockDelProducto(idProducto)} {self.obtenerNombreProducto(idProducto)} ***")
                            self.calcularPrecioProducto(idProducto, unidadesSolicitadas)
                    except ValueError:
                        print (f"*** {unidadesSolicitadas} es un formato erróneo. Solo se admiten números. ***")
                else:
                    print(f"*** No hay stock de {self.obtenerNombreProducto(idProducto)} ***\n")
            else:
                print(f"*** {idProducto} no es un ID válido. El rango es 0 a {len(self.stockTotal)-1} ***")
                self.anadirACarritoCliente()
        except ValueError:
            print ("*** Formato de ID erróneo. Solo se admiten números. ***")
            self.anadirACarritoCliente()
    
    def calcularPrecioProducto(self, idProducto, unidadesSolicitadas):
        nombreProducto = self.obtenerNombreProducto(idProducto)
        precioDelProducto = self.stockTotal[idProducto][1]
        stockProducto = self.mostrarStockDelProducto(idProducto)        
        print(f"El valor por unidad es {precioDelProducto}")
        subtotal = precioDelProducto * unidadesSolicitadas
        print(f"\nMonto total para {unidadesSolicitadas} {nombreProducto}: ${subtotal}\n")
        return subtotal

    def mostrarStockDelProducto(self, idProducto):
        stockProducto = self.stockTotal[idProducto][2]
        print(f"\nEl stock actual de {self.stockTotal[idProducto][0]} es: {stockProducto}")
        return stockProducto
    
    def obtenerNombreProducto(self, idProducto):
        nombreDelProducto = self.stockTotal[idProducto][0]
        return nombreDelProducto

    # Opción 5.
    def retirarDelCarritoCliente(self):
        pass

    # Opción 6. Calcula la suma total que debe abonar
    def cobrarProductos(self):
        pass
    
    # Opción 7. Mostrar los productos en el carrito del cliente
    def mostrarCarritoCliente(self):
            print(f"\nLos productos en el carrito son: {self.carritoCliente}")

    def mostrarMenu(self):
        print ("\nBienvenido a Ferretería Pirulito: ")
        print ("1) Mostrar lista de productos en stock.")
        print ("2) Agregar un producto al stock de la tienda")
        print ("3) Remover un producto del stock de la tienda")
        print ("4) Añadir un producto al carrito del cliente.")
        print ("5) Retirar un producto del carrito del cliente.")
        print ("6) Cobrar todos los productos.")
        print ("7) Mostrar carrito cliente.")
        print ("8) Salir")
        try:
            opcion = int(input("Elija una opción por favor: "))
            return opcion
        except ValueError:
            print ("\n*** Se introdujo un formato erróneo. Solo se admiten números. ***")


def procesarOpcion(opcion, miniCobrador):
    if opcion == 1:
        miniCobrador.listaDeProductos()
    elif opcion == 2:
        miniCobrador.agregarProductoAlStock()
    elif opcion == 3:
        miniCobrador.removerProductoDelStock()
    elif opcion == 4:
        miniCobrador.anadirACarritoCliente()
    elif opcion == 5:
        miniCobrador.retirarDelCarritoCliente()
    elif opcion == 6:
        miniCobrador.cobrarProductos()
    elif opcion == 7:
        miniCobrador.mostrarCarritoCliente()
    else:
        print(f"*** {opcion} es una opción incorrecta ***")


miniCobrador = MiniCobrador()

while(True):
    opcion = miniCobrador.mostrarMenu()
    if opcion == 8:
        break
    else:
        procesarOpcion(opcion, miniCobrador)
