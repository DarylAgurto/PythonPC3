class Producto:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo

    def __str__(self):
        return f"Producto: {self.nombre}, Código: {self.codigo}"

class Catalogo:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_catalogo(self):
        print("Catálogo de productos:")
        for producto in self.productos:
            print(producto)
