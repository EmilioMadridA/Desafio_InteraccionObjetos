Clases externas
from tienda import Restaurante, Supermercado, Farmacia
from producto import Producto

# Funcion
def validar(elemento, valores_posibles):
    """Metodo que verifica si el elemento dado se encuentra dentro de una lista de valores posibles.

        Args:
        elemento (str): El valor a validar entre los tios de tienda.
        valores_posibles (list): Lista que contiene los elementos validos, a evaluar según "elemento".

        Returns:
        elemento (str): Retorna el elemento ingresado
        """
    while elemento not in valores_posibles:
        print(f"Opción no válida, ingrese una de las opciones válidas: {', '.join(valores_posibles)} \n")
        elemento = input('Ingresa una Opción: \n').lower()
    return elemento

# Funcion
def main():
    """
    Función base, que implementa la lógica de interacción del usuario con el sistema de tiendas.
    """
    # Solicitar y validar el tipo de tienda.
    tipo_tienda = input("Ingrese el tipo de tienda (Restaurante, Supermercado, Farmacia): \n").lower()
    tipo_tienda2 = validar(tipo_tienda, ['restaurante', 'supermercado', 'farmacia'])
    # Solicitar datos de la tienda.
    nombre = input("Ingrese el nombre de la tienda: ")
    costo_delivery = float(input("Ingrese el costo de delivery: "))

    # Creación de la instancia de la tienda según el tipo.
    if tipo_tienda2 == "restaurante":
        tienda = Restaurante(nombre, costo_delivery)
    elif tipo_tienda2 == "supermercado":
        tienda = Supermercado(nombre, costo_delivery)
    else:
        tienda = Farmacia(nombre, costo_delivery)

    # Ciclo while principal de acciones.
    while True:
        accion = input("¿Qué desea hacer? (Ingresar Producto/Listar Productos/Realizar Venta/Salir): ").lower()
        # Validación de acción seleccionada por usuario.
        if accion == "ingresar producto":
            # Solicitar datos del producto y crear la instancia
            nombre_producto = input("Nombre del producto: ").lower()
            precio_producto = float(input("Precio del producto: "))
            stock_producto = int(input("Stock del producto (presione Enter para 0): ") or "0")
            producto = Producto(nombre_producto, precio_producto, stock_producto)
            tienda.ingresar_producto(producto)
        elif accion == "listar productos":
            # Listar los productos de la tienda
            print(tienda.listar_productos())
        elif accion == "realizar venta":
            # Solicitar datos de la venta y realizarla
            nombre_producto = input("Nombre del producto a vender: ").lower()
            cantidad = int(input("Cantidad: "))
            tienda.realizar_venta(nombre_producto, cantidad)
        elif accion == "salir":
            # Salir del programa
            break

# Ejecución de la función principal
main()