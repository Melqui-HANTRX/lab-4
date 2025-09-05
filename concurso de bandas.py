class participante:
    def __init__(self,nombre,institucion):
        self.nombre = nombre
        self.institucion = institucion

    def mostrar_info(self):
        return f"Nombre: {self.nombre}-Insitucion: {self.institucion}"

class Bandasescolares(participante):
    def __init__(self,nombre,institucion,categoria,puntaje):
        super().__init__(nombre,institucion)
        self._categoria = categoria
        self._puntaje = puntaje
        self.registrar_puntaje = {}

    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self,categoria):
        self._categoria = categoria

    def mostrar_info(self):
        if self._puntaje:
            return f"Nombre: {self.nombre}-Insitucion: {self.institucion} - Categoría: {self._categoria}-Puntaje total: {self._puntaje}"
        else:
            return f"Nombre: {self.nombre}-Insitucion: {self.institucion} - Categoría: {self._categoria}"


class concurso:
    def __init__(self,nombre,fecha):
        self.nombre = nombre
        self.fecha = fecha
        self.bandas = {}

    def InscribirBandas(self):

