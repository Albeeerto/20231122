"""Actividad 1 - 25 puntos
Por consola se piden como máximo 5 números hasta que pulsas q
muestra la suma de los números introducidos.
algoritmo funciona:5 puntos
algoritmo utiliza mejora en argumentos : 5 puntos
algoritmo controla errores y excepciones : 5 puntos
algoritmo aplica funciones anónimas o recursividad : 5 puntos
algoritmo resuelve una mejora de funcionalidad : 5 puntos"""


obtener_numeros = lambda: [float(input(f"Ingrese un número (o 'q' para salir, máximo 5 números): ")) for _ in range(5)]
calcular_suma = lambda numeros: sum(numeros)

def main():
    try:
        numeros = obtener_numeros()
        suma = calcular_suma(numeros)
        print(f"La suma de los números introducidos es: {suma}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()



'''Actividad 2
En consola se piden las unidades y el precio.
Estos datos permiten calcular el subtotal.
Si el día de hoy es anterior al 15 de cada mes, se aplica
un descuento del 5%
Muestra el resultado el total de la factura.

algoritmo funciona:5 puntos
algoritmo utiliza mejora en argumentos : 5 puntos
algoritmo controla errores y excepciones : 5 puntos
algoritmo aplica funciones anónimas o recursividad : 5 puntos
algoritmo resuelve una mejora de funcionalidad : 5 puntos'''


def calcular_descuento(subtotal, dia_del_mes):
    """Calcula el descuento del 5% si el día del mes es anterior al 15."""
    return subtotal * 0.05 if dia_del_mes < 15 else 0

def obtener_valor_numerico(mensaje):
    """Obtiene un valor numérico del usuario con manejo de errores."""
    while True:
        try:
            valor = float(input(mensaje))
            return valor
        except ValueError:
            print("Error: Ingrese un valor numérico válido.")

def main():
    try:
        cantidad_unidades = obtener_valor_numerico("Ingrese la cantidad de unidades: ")
        precio_por_unidad = obtener_valor_numerico("Ingrese el precio por unidad: ")
        dia_del_mes = obtener_valor_numerico("Ingrese el día del mes (1-31): ")

        subtotal = cantidad_unidades * precio_por_unidad
        descuento = calcular_descuento(subtotal, dia_del_mes)
        total = subtotal - descuento

        print(f"\nSubtotal: ${subtotal:.2f}")
        print(f"Descuento aplicado: ${descuento:.2f}")
        print(f"Total a pagar: ${total:.2f}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

''' -----Porque no he usado funcionalidades anonimas o recursivas-----
No emos usado funciones anonimas o recursivas porque:
-las funciones son especificas y no hay necesidad de reutilizar las funciones lambda en otro lugares del codigo
-La funcion 'obtener_valor_numerico' se beneficia de una definicion mas completa, espcialmente si deseamos agregar 
manejo de errores mas avanzados o funcionalidades avanzadas'''




'''
Actividad 3
En consola pides número inicial.
En consola pides número final.
Muestra una lista con todos los números pares que hay entre 
estos dos números.

algoritmo funciona:5 puntos
algoritmo utiliza mejora en argumentos : 5 puntos
algoritmo controla errores y excepciones : 5 puntos
algoritmo aplica funciones anónimas o recursividad : 5 puntos
algoritmo resuelve una mejora de funcionalidad : 5 puntos
'''

def obtener_numero(mensaje):
    """Obtiene un número del usuario con manejo de errores."""
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print("Error: Ingrese un número entero válido.")

def numeros_pares_entre(inicio, fin):
    """Genera una lista con todos los números pares entre dos números dados."""
    return [num for num in range(inicio, fin + 1) if num % 2 == 0]

def main():
    try:
        inicio = int(input("Ingrese el número inicial: "))
        fin = int(input("Ingrese el número final: "))

        if inicio <= fin:
            lista_pares = numeros_pares_entre(inicio, fin)
            if lista_pares:
                print(f"\nNúmeros pares entre {inicio} y {fin}: {lista_pares}")
            else:
                print(f"No hay números pares entre {inicio} y {fin}.")
        else:
            print("Error: El número inicial debe ser menor o igual al número final.")

    except ValueError:
        print("Error: Ingrese números enteros válidos.")

if __name__ == "__main__":
    main()



'''--No emos usado funciones anonimas o recursivas por que:---
-Legibilidad
-Simplicidad
-Manejo de errores
-Recursion 
'''




'''Actividad 4
Crea un módulo con las siguientes clases
Mesa
Silla
Lampara
las tres clases tiene como atributo color y precio.
En otro módulo importa únicamente la clase Silla y crea dos sillas. Una de color azul y otra roja con precios de 9.95

algoritmo funciona:5 puntos
algoritmo utiliza características de POO : 5 puntos
algoritmo controla errores y excepciones : 5 puntos
algoritmo aplica enumeradores o similar para Color : 5 puntos
algoritmo resuelve una mejora de funcionalidad : 5 puntos'''


from enum import Enum

class Color(Enum):
    AZUL = "azul"
    ROJO = "rojo"
    VERDE = "verde"


class Mueble:
    def __init__(self, color, precio):
        self.color = color
        self.precio = precio

    def __str__(self):
        return f"Color: {self.color.name.title()}, Precio: {self.precio:.2f}"

class Mesa(Mueble):
    pass

class Silla(Mueble):
    pass

class Lampara(Mueble):
    pass











