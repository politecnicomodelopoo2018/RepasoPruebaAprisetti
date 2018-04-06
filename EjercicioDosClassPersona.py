import datetime
from EjercicioDosClassPlato import Plato

class Persona(object):

    def __init__(self, nombre = None, fechaDeNacimiento = None, cantCaloriasConsumidas = None):

        self.nombre = nombre
        self.fechaDeNacimiento = fechaDeNacimiento
        self.cantCaloriasConsumidas = cantCaloriasConsumidas

        self.listaDePlatosConsumidos = []

    def setNombre(self, nombreAIngresar):
        self.nombre = nombreAIngresar

    def setFechaDeNacimiento(self, fechaDeNacimientoAIngresar):
        self.fechaDeNacimiento = fechaDeNacimientoAIngresar

    def setPlatoConsumido(self, platoConsumidoAIngresar):
        self.listaDePlatosConsumidos.append(platoConsumidoAIngresar)

    def getCaloriasConsumidasEnTotal(self):
        calorias = 0

        for item in self.listaDePlatosConsumidos:
            calorias += item.cantCals

        self.cantCaloriasConsumidas = calorias
        return self.cantCaloriasConsumidas