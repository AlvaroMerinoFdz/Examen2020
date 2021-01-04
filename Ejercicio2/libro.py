class Libro:
    def __init__(self, identificador, isbn, titulo, editorial, idioma, autor, genero):
        self._identificador = identificador
        self._isbn = isbn
        self._titulo = titulo
        self._editorial = editorial
        self._idioma = idioma
        self._autor = autor
        self._genero = genero

    def set_identificador(self, identificador):
        self._identificador = identificador

    def set_isbn(self, isbn):
        self._isbn = isbn

    def set_titulo(self, titulo):
        self._titulo = titulo

    def set_editorial(self, editorial):
        self._editorial = editorial

    def set_idioma(self, idioma):
        self._idioma = idioma

    def set_autor(self, autor):
        self._autor = autor

    def set_genero(self, genero):
        self._genero = genero

    def get_identificador(self):
        return self._identificador

    def get_isbn(self):
        return self._isbn

    def get_titulo(self):
        return self._titulo

    def get_editorial(self):
        return self._editorial

    def get_idioma(self):
        return self._idioma

    def get_autor(self):
        return self._autor

    def get_genero(self):
        return self._genero

    def __str__(self):
        clase = type(self).__name__
        mensaje = "{0}= Identificador: {1}"
        return mensaje.format(clase, self.get_identificador())
