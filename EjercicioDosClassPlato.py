class Plato(object):

    def __init__(self, nombre = None, cantCals = None):

        self.nombre = nombre
        self.cantCals = cantCals

    def setNombre(self, nombreAIngresar):
        self.nombre = nombreAIngresar

    def setCantCals(self, cantCalsAIngresar):
        self.cantCals = cantCalsAIngresar
