from Ejercicio1.persona import Persona


class Delincuente(Persona):
    def __init__(self, identificador, *args):
        Persona.__init__(self, identificador)
        self._delitos = args

    def get_delitos(self):
        return self._delitos

    def set_delitos(self, delitos):
        self._delitos = delitos
