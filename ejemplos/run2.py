"""

"""
# Crear dos objetos de la clase 02

class Celulares:
# objeto 01

    def __init__(self, marc, m):
        self.marca = marc
        self.modelo = m

    def __str__(self):
        return f"Teléfono: {self.marca} \nModelo: {self.modelo}"


# crear
telefono1 = Celulares("Apple", "Iphone 13")
# Presentar objeto; usar el método __st__
print(telefono1)
# objeto 02


# crear ingresando valores por teclado
marca2 = input("Ingresa la marca del teléfono: ")
modelo2 = input("Ingresa el modelo del telefono: ")


telefono2 = Celulares(marca2, modelo2)

# Presentar objeto; usar el método __st__
print(telefono2)

