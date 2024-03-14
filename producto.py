# Definicion de clase
class Producto:
    """ 
    Clase cuyo proposito es la representación de un producto, con nombre, precio y stock.
    """
    def __init__(self, nombre, precio, stock=0):
        """ Metodo de inicialización de la instancia Producto.

        Args:
            nombre (str): Corresponde al nombre del producto, ingresado por usuario.
            precio (float): Corresponde al precio del producto, ingresado por usuario.
            stock (int): Corresponde al stock del producto, ingresado por usuario. Defaults to 0.
        """
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock

    @property
    def nombre(self):
        """ Metodo que retorna el nombre del producto.

        Returns:
            str: Retorna el nombre del producto.
        """
        return self.__nombre

    @property
    def precio(self):
        """ Metodo que retorna el precio del producto.

        Returns:
            float: Retorna el precio del producto.
        """
        return self.__precio

    @property
    def stock(self):
        """ Metodo que retorna el stock del producto.

        Returns:
            int: Retorna el stock del producto al momento de llamarlo.
        """
        return self.__stock

    @stock.setter
    def stock(self, valor):
        """ Metodo que establece el stock del producto.

        Args:
            valor (int): El valor correspondiente al stock ingresado y/o modificado.
        """
        self.__stock = max(0, valor)

    def __eq__(self, otro):
        """ Metodo que verifica si este producto es igual a otro basado en su nombre.

        Args:
            otro (object): Otro objeto instancia de Producto.

        Returns:
            bool: Retorna True en caso de que ambos objetos tengan el mismo nombre, False en caso contrario.
        """
        return self.__nombre == otro.__nombre

    def __add__(self, otro):
        """ Metodo que suma el stock de otro producto al stock actual si los productos son iguales.

        Args:
            otro (object): Otro objeto instancia de Producto.
        """
        if self == otro:
            self.stock += otro.stock
        
    def __str__(self):
        """ Metodo que retorna una representación en cadena del producto.

        Returns:
            str: Una cadena de texto que representa el producto, incluyendo sus atributos.
        """
        return f"Producto: {self.__nombre}, Precio: {self.__precio}, Stock: {self.__stock}"