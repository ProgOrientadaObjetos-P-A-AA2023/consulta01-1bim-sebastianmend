"""

"""

# Crear dos clases en Python
# Usted defina el nombre y los atributos
# Puede usar las mismas clases usadas en Java en los ejemplos estudiados

# clase 01

class Telefonos:
    marca = ''
    imei = ''
    color = ''
    modelo = ''

    def __init__(self, marc, im, c, m):
        self.marca = marc
        self.imei = im
        self.color = c
        self.modelo = m

    def __str__(self):
        cadena = "Marca: {}\nimei: {}\nColor: {}\nMdelo: {}".format(
            self.marca, self.imei, self.color, self.modelo)
        return cadena




# clase 02
class Colegios:
    nombre = ''
    cantAlumn = 0
    tipo = ''

    def __init__(self, nom, c, tp):
        self.nombre = nom
        self.cantAlumn = c
        self.tipo = tp

    def __str__(self):
        cadena = "Colegios\nNombre del colegio: {}\nCantidad de Alumnos: {}\nTipo: {}".format(
            self.nombre, self.cantAlumn, self.tipo)
        return cadena