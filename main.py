

import os

from problema1 import resolver_problema1
from problema2 import Circulo
from problema3 import Catalogo, Producto
from operaciones import dividir

if __name__ == "__main__":
    # 1
    resolver_problema1()

    #2
    circulo = Circulo(5)
    print(f"Área del círculo: {circulo.calcular_area()}")

    #3
    catalogo = Catalogo()
    producto1 = Producto("Aceite", "PERU-0001-2023")
    producto2 = Producto("Filtro de aire", "MEXICO-0002-2023")
    catalogo.agregar_producto(producto1)
    catalogo.agregar_producto(producto2)
    catalogo.mostrar_catalogo()

    #4
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = dividir(num1, num2)
        print(f"Resultado de la división: {resultado}")
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")
    except ValueError:
        print("Error: Ingrese números válidos.")
    else:
        print(f"Directorio de trabajo: {os.getcwd()}")
    finally:
        print("Proceso terminado")

    #5
    producto3 = Producto("Batería", "ARGENTINA-0003-2023")
    print(producto3)

    #7
    class Phone:
        def __init__(self, brand, model):
            self.brand = brand
            self.model = model
            self.battery_percentage = 100

        def make_call(self):
            print(f"Calling from {self.brand} {self.model}")

        def charge_battery(self):
            self.battery_percentage = 100

    #8
    class Persona:
        def __init__(self, nombre, edad, ciudad):
            self.nombre = nombre
            self.edad = edad
            self.ciudad = ciudad

    # Instanciar datos de Persona desde el teclado
    nombre = input("Ingrese el nombre: ")
    edad = int(input("Ingrese la edad: "))
    ciudad = input("Ingrese la ciudad: ")
    persona = Persona(nombre, edad, ciudad)
