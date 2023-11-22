from simulacion import Silla, Color

from colorama import Fore, Style  # Añade estas líneas

def mostrar_info_silla(silla):
    # Utiliza Fore para cambiar el color del texto en la consola
    print(f"Color: {Fore.BLUE if silla.color == Color.AZUL else Fore.RED}{silla.color.name.title()}{Style.RESET_ALL}, Precio: {silla.precio:.2f}")

# Crear dos instancias de la clase Silla usando enumeradores para el color
silla_azul = Silla(color=Color.AZUL, precio=9.95)
silla_roja = Silla(color=Color.ROJO, precio=9.95)

# Mostrar información de las sillas con colores en la consola
mostrar_info_silla(silla_azul)
mostrar_info_silla(silla_roja)

