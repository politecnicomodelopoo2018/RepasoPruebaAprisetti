
class ChequeoCorporal(object):

    def __init__(self, altura = None, peso = None, fechaMedicion = None):

        self.altura = altura
        self.peso = peso
        self.fechaMedicion = fechaMedicion

    def setAltura(self, alturaAIngresar):
        self.altura = alturaAIngresar

    def setPeso(self, pesoAIngresar):
        self.peso = pesoAIngresar

    def setFechaMedicion(self, fechaMedicionAIngresar):
        self.fechaMedicion = fechaMedicionAIngresar
