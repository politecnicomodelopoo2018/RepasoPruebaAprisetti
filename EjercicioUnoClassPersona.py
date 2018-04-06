from EjercicioUnoClassChequeoCorporal import ChequeoCorporal
import datetime

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
        return promedioAnual

    def getAlturaPromedio(self, año):
        sumaAltura = 0
        cantidadMediciones = 0

        for item in self.listaChequeoCorporal:
            if item.fechaMedicion.year == año:
                sumaAltura += item.altura
                cantidadMediciones += 1

        promedioAnual = sumaAltura / cantidadMediciones
        return promedioAnual

    def getPorcentajeCrecimientoPeso(self, primerAño, ultimoAño):
        listaDelPrimerAño = []
        listaDelUltimoAño = []

        for item in self.listaChequeoCorporal:
            if item.fechaMedicion.year == primerAño:
                listaDelPrimerAño.append(item.fechaMedicion)
            elif item.fechaMedicion.year == ultimoAño:
                listaDelUltimoAño.append(item.fechaMedicion)

        ultimaFechaDelPrimerAño = max(listaDelPrimerAño)
        ultimaFechaDelUltimoAño = max(listaDelUltimoAño)

        pesoPrimerAño = 0
        pesoUltimoAño = 0

        for item in self.listaChequeoCorporal:
            if item.fechaMedicion == ultimaFechaDelPrimerAño:
                pesoPrimerAño = item.peso
            elif item.fechaMedicion == ultimaFechaDelUltimoAño:
                pesoUltimoAño = item.peso

        porcentajeDeCrec = ((pesoUltimoAño * 100)/pesoPrimerAño) - 100
        return porcentajeDeCrec

    def getPorcentajeCrecimientoAltura(self, primerAño, ultimoAño):
        listaDelPrimerAño = []
        listaDelUltimoAño = []

        for item in self.listaChequeoCorporal:
            if item.fechaMedicion.year == primerAño:
                listaDelPrimerAño.append(item.fechaMedicion)
            elif item.fechaMedicion.year == ultimoAño:
                listaDelUltimoAño.append(item.fechaMedicion)

        ultimaFechaDelPrimerAño = max(listaDelPrimerAño)
        ultimaFechaDelUltimoAño = max(listaDelUltimoAño)

        alturaPrimerAño = 0
        alturaUltimoAño = 0

        for item in self.listaChequeoCorporal:
            if item.fechaMedicion == ultimaFechaDelPrimerAño:
                alturaPrimerAño = item.altura
            elif item.fechaMedicion == ultimaFechaDelUltimoAño:
                alturaUltimoAño = item.altura

        porcentajeDeCrec = ((alturaUltimoAño * 100) / alturaPrimerAño) - 100
        return porcentajeDeCrec