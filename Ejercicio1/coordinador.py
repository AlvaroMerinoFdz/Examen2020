from Ejercicio1.ciberpolicia import Ciberpolicia
from Ejercicio1.delincuente import Delincuente


class Coordinador(Ciberpolicia):
    def __init__(self, nombre, identificador, numPlaca):
        Ciberpolicia.__init__(self, nombre, identificador, numPlaca)

    @staticmethod
    def registrarDelincuentes(nombre, *args):
        Delincuente.__init__(nombre,*args)
