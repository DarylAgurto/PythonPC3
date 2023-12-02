class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return 3.14159 * self.radio ** 2

if __name__ == "__main__":
    # Ejemplo de uso si ejecutas directamente este script
    radio_ejemplo = 5
    circulo_ejemplo = Circulo(radio_ejemplo)
    print(f"Área del círculo con radio {radio_ejemplo}: {circulo_ejemplo.calcular_area()}")
