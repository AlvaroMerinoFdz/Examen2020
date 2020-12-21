class Persona:
    def __init__(self, identificador):
        self._identificador = identificador

    def set_identificador(self, identificador):
        self._identificador = identificador

    def get_identificador(self):
        return self._identificador
    def __str__(self):
        clase = type(self).__name__
        mensaje = "Identificador: {1}"
        return mensaje.format(clase,self.get_identificador())

