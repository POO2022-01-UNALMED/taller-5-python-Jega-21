class Zoologico: # Clase.

    # Atributos.
    def __init__(self, nombre, ubicacion):
        self._nombre = nombre
        self._ubicacion = ubicacion
        self._zonas = []

    # Getters and Setters.
    def getNombre(self):
        return self._nombre
    def setNombre(self, nombre):
        self._nombre = nombre

    def getUbicacion(self):
        return self._ubicacion
    def setUbicacion(self, ubicacion):
        self._ubicacion = ubicacion

    def getZona(self):
        return self._zonas
    def setZona(self, zonas):
        self._zonas = zonas

    # Metodos.
    def agregarZonas(self, zona):
        self._zonas.append(zona)

    def cantidadTotalAnimales(self):
        sum = 0
        for i in self._zonas:
            sum += len(i._animales)
        return sum