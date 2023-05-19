"""

"""
# Crear dos objetos de la clase 02

from mis_clases import Colegios

# objeto 01

# crear

cole1 = Colegios("Mater Dei",100,"Fiscomisional")

# Presentar objeto; usar el método __st__

print(str(cole1))

# objeto 02

print("Ingrese el nombre del colegio")
nom = input()
print("ingrese la cantidad de alumnos")
cant = int(input())
print("Ingrese el tipo de institución:")
tp = input()

# crear ingresando valores por teclado

cole2 =Colegios(nom,cant,tp)

# Presentar objeto; usar el método __st__

print(str(cole2))