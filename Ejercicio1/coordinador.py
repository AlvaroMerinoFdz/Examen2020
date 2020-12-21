from Ejercicio1.ciberpolicia import Ciberpolicia


class Coordinador(Ciberpolicia):
    def __init__(self, nombre, identificador, numPlaca):
        Ciberpolicia.__init__(self, nombre, identificador, numPlaca)

    def registrarDelincuentes(self):
        print("Hay que hacerlo")
