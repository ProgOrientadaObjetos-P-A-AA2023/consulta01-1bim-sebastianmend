"""

"""
# Crear dos objetos de la clase 01

class Alumno:
# objeto 01

    def __init__(self, nom, cal):
        self.nombre = nom
        self.calificacion = cal

    def __str__(self):
        return f"Alumno: {self.nombre} \nNota: {self.calificacion}"


# crear
al1 = Alumno("Michelena", 9.99)
# Presentar objeto; usar el método __st__
print(al1)
# objeto 02


# crear ingresando valores por teclado

nombre2 = input("Ingresa el nombre del segundo estudiante: ")
calificacion2 = int(input("Ingresa la calificacion obtenida: "))
al2 = Alumno(nombre2, calificacion2)

# Presentar objeto; usar el método __st__
print(al2)


