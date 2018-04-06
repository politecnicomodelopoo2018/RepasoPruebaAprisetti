from EjercicioUnoClassChequeoCorporal import ChequeoCorporal
from EjercicioUnoClassPersona import Persona
import datetime
from random import randint

ejemplar = Persona()
chequeoPersona = []


ejemplar.setNombre("Pepe")
ejemplar.setApellido("Lopez")
nacimiento = datetime.date(2000, 7, 30)
ejemplar.setFechaDeNacimiento(nacimiento)

for i in range(365):

    randYear = randint(2003, 2014)
    randMonth = randint(1, 12)
    randDay = randint(1, 28)
    randPeso = randint(50, 101)
    randAltura = randint(155, 200)

    fechaMedicion = datetime.date(randYear, randMonth, randDay)

    medicion = ChequeoCorporal()

    medicion.setFechaMedicion(fechaMedicion)
    medicion.setAltura(randAltura)
    medicion.setPeso(randPeso)

    ejemplar.setListaChequeo(medicion)

alturaPromedio = ejemplar.getAlturaPromedio(2005)
pesoPromedio = ejemplar.getPesoPromedio(2005)
porcentajeAltura = ejemplar.getPorcentajeCrecimientoAltura(2005, 2008)
porcentajePeso = ejemplar.getPorcentajeCrecimientoPeso(2005, 2008)

print("Altura Promedio: ", alturaPromedio, "cm")
print("Peso Promedio: ", pesoPromedio, "kg")
print("Porcentaje Altura: ", porcentajeAltura, "%")
print("Porcentaje Peso: ", porcentajePeso, "%")