import datetime
from random import randint
from EJercicioDosClassFamilia import  Familia
from EjercicioDosClassPersona import Persona
from EjercicioDosClassPlato import  Plato

primeraPersona = Persona()
segundaPersona = Persona()
terceraPersona = Persona()

primeraPersona.setNombre("Pedro")
primeraPersona.setFechaDeNacimiento(datetime.date(1987, 8, 10))
segundaPersona.setNombre("Maria")
segundaPersona.setFechaDeNacimiento(datetime.date(1982, 10, 14))
terceraPersona.setNombre("Juan")
terceraPersona.setFechaDeNacimiento(datetime.date(2000, 3, 7))

unidadFamiliar = Familia()

unidadFamiliar.setNombreFamilia("Lopez")


for i in range(7):
    primerPlato = Plato()
    primerPlato.setNombre("Desayuno")
    primerPlato.setCantCals((randint(300, 600)))
    primeraPersona.setPlatoConsumido(primerPlato)
for j in range(7):
    segundoPlato = Plato()
    segundoPlato.setNombre("Desayuno")
    segundoPlato.setCantCals((randint(300, 600)))
    segundaPersona.setPlatoConsumido(segundoPlato)
for h in range(7):
    tercerPlato = Plato()
    tercerPlato.setNombre("Desayuno")
    tercerPlato.setCantCals((randint(300, 600)))
    terceraPersona.setPlatoConsumido(tercerPlato)

print("Cantidad consumidas por: ", primeraPersona.nombre, " ", primeraPersona.getCaloriasConsumidasEnTotal(), "kcals")
print("Cantidad consumidas por: ", segundaPersona.nombre, " ", segundaPersona.getCaloriasConsumidasEnTotal(), "kcals")
print("Cantidad consumidas por: ", terceraPersona.nombre, " ", terceraPersona.getCaloriasConsumidasEnTotal(), "kcals")

unidadFamiliar.setListaDeIntegrante(primeraPersona)
unidadFamiliar.setListaDeIntegrante(segundaPersona)
unidadFamiliar.setListaDeIntegrante(terceraPersona)

print("La persona que menos consumio: ", unidadFamiliar.getPersonaQueMenosConsumio())
print("La persona que mas consumio: ", unidadFamiliar.getPersonaQueMasConsumio())
print("Se consumieron en promedio: ", unidadFamiliar.getPromedioCals(), "kcals")