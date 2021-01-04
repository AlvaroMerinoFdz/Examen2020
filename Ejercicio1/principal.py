import json

from Ejercicio1.ciberpolicia import Ciberpolicia
from Ejercicio1.coordinador import Coordinador
from Ejercicio1.patrulla import Patrulla

"""Vamos a hacer el método para importar el registro de los delincuentes en JSON"""


def escribirJSon(valores):
    datos = {valores}
    fichero = open("RegistroDelincuentes.json", "rw")
    json.dump(datos, fichero)
    fichero.close()


if "__name__" == "__main__":
    ciber1 = Ciberpolicia("Alfonso", 1, 1)
    ciber2 = Ciberpolicia("Jesus", 2, 2)
    ciber3 = Ciberpolicia("Maria", 3, 3)
    ciber4 = Ciberpolicia("Pilar", 4, 4)
    coordinador = Coordinador("Jefe", 5, 5)
    patrulla1 = Patrulla(coordinador, ciber1, ciber2, ciber3, ciber4)
    delincuente1 = coordinador.registrarDelincuentes("Josete", "Robar galllinas")
    escribirJSon(delincuente1)
