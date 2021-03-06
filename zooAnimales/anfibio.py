from zooAnimales.animal import Animal

class Anfibio(Animal): # Clase.
    _listado = []
    ranas = 0
    salamandras = 0

    # Atributos.
    def __init__(self, nombre, edad, habitat, genero, colorPiel, venenoso):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPiel = colorPiel
        self._venenoso = venenoso
        Anfibio._listado.append(self)

    # Metodos.
    @staticmethod
    def cantidadAnfibios():
        return len(Anfibio._listado)

    def movimiento():
        return "saltar"
        
    @classmethod
    def crearRana(cls, nombre, edad, genero):
        cls.ranas += 1
        return Anfibio(nombre, edad, "selva", genero, "rojo", True)

    @classmethod
    def crearSalamandra(cls, nombre, edad, genero):
        cls.salamandras += 1
        return Anfibio(nombre, edad, "selva", genero, "negro y amarillo", False)

    # Getters and Setters
    @classmethod
    def getListado(cls):
        return cls._listado
    def getColorPiel(self):
        return self._colorPiel
    def isVenenoso(self):
        return self._venenoso

    @classmethod
    def setListado(cls, listado):
        cls._listado = listado
    def setColorPiel(self, colorPiel):
        self._colorPiel = colorPiel
    def setVenenoso(self, venenoso):
        self._venenoso = venenoso