"""

"""

# Crear dos clases en Python
# Usted defina el nombre y los atributos
# Puede usar las mismas clases usadas en Java en los ejemplos estudiados

# clase 01
class Persona:
    def __init__(self, per1):
        self.per1 = per1

    def saludo(self):

        print(f"Bienvenido, {self.per1} a este apocento de las matemáticas")


per1 = Persona("Juan Gonzalez")
per1.saludo()



# clase 02
class triang:
    """
    Defineel área de un triángulo.
    """
    def __init__(self, b, h):
        self.b = b
        self.h = h


    def area(self):
        return (self.b * self.h)/2

triang =triang(10, 10)
print("Área del triángulo es: ", triang.area(), "metros")