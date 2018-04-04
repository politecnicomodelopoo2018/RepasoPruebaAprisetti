from EjercicioUnoClassChequeoCorporal import ChequeoCorporal

class Persona(object):

    def __init__(self, nombre = None, apellido = None, fechaDeNacimiento = None):

        self.nombre = nombre
        self.apellido = apellido
        self.fechaDeNacimiento = fechaDeNacimiento

        self.listaChequeoCorporal = []

    def setNombre(self, nombreAIngresar):
        self.nombre = nombreAIngresar

    def setApellido(self, apellidoAIngresar):
        self.apellido = apellidoAIngresar

    def setFechaDeNacimiento(self, fechaDeNacimientoAIngresar):
        self.fechaDeNacimiento = fechaDeNacimientoAIngresar

    def setListaChequeo(self, chequeoAIngresar):
        self.listaChequeoCorporal.append(chequeoAIngresar)

    def getPesoPromedio(self, año):
        sumaPeso = 0
        cantidadPesos = 0

        for item in self.listaChequeoCorporal:
            if item.fechaMedicion.year == año:
                sumaPeso += item.peso
                cantidadPesos += 1

        promedioAnual = sumaPeso/cantidadPesos
