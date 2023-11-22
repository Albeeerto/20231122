#vamos a utilizar el contenido del modulo ejemplo2

import ejemplo2
from ejemplo3 import Pais

#uso de variables
ejemplo2.alumnos.update({"luis":"dam"})
print(ejemplo2.alumnos)

#uso de funciones
ejemplo2.calcular_cubo()

#uso de una clase
producto1=ejemplo2.Producto("camisas", 50)

francia=Pais("France","Paris")