class MiniCobrador:

    def __init__(self):
        # [NombreDelProducto, Precio, StockDisponible]
        self.stockTotal = [["Pinza Fuerza", 700, 5],
                        ["Pinza Punta", 750, 8],
                        ["Taladro", 2500, 6],
                        ["Destornillador", 450, 7]]

    # Opción 1. Muestra la lista de productos en stock
    def listaDeProductos(self):
        print (f"Lista de productos: NombreDelProducto | Precio x Unidad | Stock Disponible\n")
        i = 0
        while i < len(self.stockTotal):
            print (f"ID:[{i}] {self.stockTotal[i][0]} | ${self.stockTotal[i][1]} | {self.stockTotal[i][2]} unidades disponibles")
            i += 1
        

    # Opción 2.
    def agregarProductoAlStock(self):
        pass

    # Opción 3.
    def removerProductoDelStock():
        print ("algo")

    # Opción 4.
    def anadirACuentaCliente(self):
        IDProducto = int(input("Elija el ID del producto: "))
        nombreDelProducto = self.stockTotal[IDProducto][0]
        precioDelProducto = self.stockTotal[IDProducto][1]
        stockDelProducto = self.stockTotal[IDProducto][2]
        print(f"\nEl stock actual de {nombreDelProducto} es: {stockDelProducto}")
        print(f"Y el valor por unidad es {precioDelProducto}")
        unidadesSolicitadas = int(input("\nElija la cantidad unidades: "))
        subtotal = precioDelProducto * unidadesSolicitadas
        print(f"\nMonto total para {unidadesSolicitadas} de {nombreDelProducto}: ${subtotal}\n")

    # Opción 5.
    def retirarDeCuentaCliente(self):
        print ("algo")

    # Opción 6. Calcula la suma total que debe abonar
    def cobrarProductos(self):
        print("algo")

    def mostrarMenu(self):
        print ("Bienvenido a Ferretería Pirulito: ")
        print ("1) Mostrar lista de productos.")
        print ("2) Agregar un producto a la lista.")
        print ("3) Remover un producto de la lista.")
        print ("4) Añadir un producto a una cuenta cliente.")
        print ("5) Retirar un producto de una cuenta cliente.")
        print ("6) Cobrar todos los productos.")
        opcion = int(input("Elija una opción por favor: "))
        return opcion


def procesarOpcion(opcion, miniCobrador):
    if opcion == 1:
        miniCobrador.listaDeProductos()
    elif opcion == 2:
        miniCobrador.agregarProductoAlStock()
    elif opcion == 3:
        miniCobrador.removerProductoDelStock()
    elif opcion == 4:
        miniCobrador.anadirACuentaCliente()
    elif opcion == 5:
        miniCobrador.retirarDeCuentaCliente()
    elif opcion == 6:
        miniCobrador.cobrarProductos()
    else:
        print(f"{opcion} es una opción incorrecta")


miniCobrador = MiniCobrador()

opcion = miniCobrador.mostrarMenu()

procesarOpcion(opcion, miniCobrador);
