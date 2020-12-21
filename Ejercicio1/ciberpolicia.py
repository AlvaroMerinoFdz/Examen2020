from Ejercicio1.persona import Persona


class Ciberpolicia(Persona):
    def __init__(self, nombre, identificador, numPlaca):
        self._nombre = nombre
        Persona.__init__(self, identificador)
        self._numPlaca = numPlaca

    def get_nombre(self):
        return self._nombre

    def get_numPlaca(self):
        return self._numPlaca

    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_numPlaca(self, numPlaca):
        self._numPlaca = numPlaca

    def __str__(self):
        clase = type(self).__name__
        mensaje = "{0}: Nombre: {1}, Identificador: {2}, Número de placa: {3}"
        return mensaje.format(clase, self.get_nombre(), self.get_identificador(), self.get_numPlaca())
