# Funciones, clases y metodos externos
from abc import ABC, abstractmethod
from producto import Producto

# Definicion de clase
class Tienda(ABC):
    """ 
    Clase abstracta que tiene como proposito representar una tienda genérica.
    """
    def __init__(self, nombre, costo_delivery):
        """ Metodo que inicializa una nueva instancia de la clase Tienda.

        Args:
            nombre (str): El nombre de la tienda, entregado por el usuario.
            costo_delivery (float): El costo asociado al delivery.
        """
        self.nombre = nombre
        self.costo_delivery = costo_delivery
        self.productos = []

    def ingresar_producto(self, nuevo_producto):
        """ Metodo que añade un producto a la lista de productos de la tienda o actualiza su stock si ya existe.

        Args:
            nuevo_producto (object): El producto a añadir o al que se debe actualizar su stock.
        """
        encontrado = next((p for p in self.productos if p.nombre == nuevo_producto.nombre), None)
        if encontrado:
            encontrado.stock += nuevo_producto.stock
        else:
            self.productos.append(nuevo_producto)

    @abstractmethod
    def listar_productos(self):
        """
        Metodo abstracto para listar los productos disponibles en la tienda.
        """
        pass

    @abstractmethod
    def realizar_venta(self, nombre_producto, cantidad):
        """ Metodo abstracto querealiza una venta de un producto específico en la cantidad determinada.

        Args:
            nombre_producto (str): Nombre del producto a vender.
            cantidad (int): La cantidad del producto correspondiente a vender.
        """
        pass

# Definicion de clase
class Restaurante(Tienda):
    """ 
    Clase de representación de una tienda de tipo Restaurante.
    """
    def ingresar_producto(self, nuevo_producto):
        """ Metodo que añade un producto a la lista de productos del restaurante.

        Args:
            nuevo_producto (object): Corresponde al producto a añadir.
        """
        nuevo_producto.stock = 0  # Restaurante siempre tiene stock 0
        super.agregar_producto(nuevo_producto)

    def listar_productos(self):
        """ Metodo que enlista los productos disponibles en el restaurante.

        Returns:
            str: Cadena de texto en forma de lista de los productos disponibles.
        """
        return "\n".join([f"{p.nombre} - Precio: {p.precio}" for p in self.productos])

    def realizar_venta(self, nombre_producto, cantidad):
        """ Metodo que simula la realización de una venta en el restaurante. No modifica el stock.

        Args:
            nombre_producto (str): Corresponde al nombre del producto a vender.
            cantidad (int): Corresponde a la cantidad del producto en cuestión.
        """
        print("Venta realizada en restaurante.")

# Definicion de clase
class Supermercado(Tienda):
    """ 
    Clase de representación de una tienda de tipo Supermercado.
    """
    def listar_productos(self):
        """ Metodo que enlista los productos disponibles en el supermercado.

        Returns:
            str: Cadena de texto en forma de lista de los productos disponibles.
        """
        productos_str = []
        for producto in self.productos:
            mensaje_stock = " - Pocos productos disponibles" if producto.stock < 10 else ""
            productos_str.append(f"{producto.nombre} - Stock: {producto.stock}{mensaje_stock}")
        return "\n".join(productos_str)

    def realizar_venta(self, nombre_producto, cantidad):
        """ Metodo que simula la realización de una venta en el supermercado.

        Args:
            nombre_producto (str): Corresponde al nombre del producto a vender.
            cantidad (int): Corresponde a la cantidad del producto en cuestión.
        """
        producto = next((p for p in self.productos if p.nombre == nombre_producto), None)
        if producto and producto.stock >= cantidad:
            producto.stock -= cantidad
            print(f"Venta realizada: {cantidad} unidad(es) de {nombre_producto}.")
        elif producto:
            print(f"Solo se vendieron {producto.stock} unidades de {nombre_producto} debido a falta de stock.")
            producto.stock = 0
        else:
            print("Producto no encontrado.")

# Definicion de clase
class Farmacia(Tienda):
    """ 
    Clase de representación de una tienda de tipo Farmacia.
    """
    def listar_productos(self):
        """ Metodo que enlista los productos disponibles en la farmacia.

        Returns:
            str: Cadena de texto en forma de lista de los productos disponibles.
        """
        productos_str = []
        for producto in self.productos:
            mensaje_precio = " - Envío gratis al solicitar este producto" if producto.precio > 15000 else ""
            mensaje_stock = " - Pocos productos disponibles" if producto.stock < 10 else ""
            productos_str.append(f"{producto.nombre} - Stock: {producto.stock}  {mensaje_precio}")
        return "\n".join(productos_str)

    def realizar_venta(self, nombre_producto, cantidad):
        """ Metodo que simula la realización de una venta en el supermercado.

        Args:
            nombre_producto (str): Corresponde al nombre del producto a vender.
            cantidad (int): Corresponde a la cantidad del producto en cuestión.
        """
        if cantidad > 3:
            print("No se puede vender más de 3 unidades por producto en la farmacia.")
            return
        producto = next((p for p in self.productos if p.nombre == nombre_producto), None)
        if producto and producto.stock >= cantidad:
            producto.stock -= cantidad
            print(f"Venta realizada: {cantidad} unidad(es) de {nombre_producto}.")
        elif producto:
            print(f"Solo se vendieron {producto.stock} unidades de {nombre_producto} debido a falta de stock.")
            producto.stock = 0
        else:
            print("Producto no encontrado.")