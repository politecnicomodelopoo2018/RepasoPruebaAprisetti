from EjercicioUnoClassPersona import Persona
from EjercicioDosClassPlato import Plato

class Familia(object):

    def __init__(self, nombreFamilia = None):

        self.nombreFamilia = nombreFamilia

        self.listaDeIntegrantes = []

    def setNombreFamilia(self, nombreFamiliaAIngresar):
        self.nombreFamilia = nombreFamiliaAIngresar

    def setListaDeIntegrante(self, integranteAIngresar):
        self.listaDeIntegrantes.append(integranteAIngresar)

    def getPromedioCals(self):

        listaCantidadConsumida = []

        for item in self.listaDeIntegrantes:
            listaCantidadConsumida.append(item.cantCaloriasConsumidas)

        cantidadDeCaloriasFamilia = sum(listaCantidadConsumida)

        promedioDeCalorias = (cantidadDeCaloriasFamilia/len(self.listaDeIntegrantes))

        return promedioDeCalorias

    def getPersonaQueMasConsumio(self):

        mayorCaloriasConsumidas = 0

        listaCalorias = []

        for item in self.listaDeIntegrantes:
            listaCalorias.append(item.cantCaloriasConsumidas)

        mayorCaloriasConsumidas = max(listaCalorias)

        for item in self.listaDeIntegrantes:
            if item.cantCaloriasConsumidas == mayorCaloriasConsumidas:
                return item.nombre

    def getPersonaQueMenosConsumio(self):

        menorCaloriasConsumidas = 0

        listaCalorias = []

        for item in self.listaDeIntegrantes:
            listaCalorias.append(item.cantCaloriasConsumidas)

        menorCaloriasConsumidas = min(listaCalorias)

        for item in self.listaDeIntegrantes:
            if item.cantCaloriasConsumidas == menorCaloriasConsumidas:
                return item.nombre