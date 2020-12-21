class Patrulla:
    def __init__(self, coordinador, *args):
        self._coordinador = coordinador
        if len(args) < 3:
            raise ValueError("Se necesitan mínimo 4 ciberpolicías")
        else:
            self._policia = args
