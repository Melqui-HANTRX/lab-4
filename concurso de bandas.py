class participante:
    def __init__(self,nombre,institucion):
        self.nombre = nombre
        self.institucion = institucion

    def mostrar_info(self):
        return f"Nombre: {self.nombre}-Insitucion: {self.institucion}"

class BandasEscolar(participante):
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

    def registrar_puntajes(self):
        print("Califique a la banda, segun los criterios del 1 al 10")

        ritmo=int(input("Ritmo: "))
        uniformidad=int(input("Uniformidad: "))
        coreo=int(input("Coreografía: "))
        alineacion=int(input("Alineación: "))
        puntualidad=int(input("Puntualidad: "))

        self._puntaje[self.nombre]={
            "ritmo": ritmo,
            "uniformidad": uniformidad,
            "coreo": coreo,
            "alineacion": alineacion,
            "puntualidad": puntualidad,
        }

        suma_puntajes=ritmo+uniformidad+coreo+alineacion+puntualidad
        self._puntaje=suma_puntajes


    def mostrar_info(self):
        if self._puntaje:
            return f"Nombre: {self.nombre}-Insitucion: {self.institucion} - Categoría: {self._categoria} - Puntaje total: {self._puntaje} - Puntaje promedio: {self._puntaje/5}"
        else:
            return f"Nombre: {self.nombre}-Insitucion: {self.institucion} - Categoría: {self._categoria}"


class concurso:
    def __init__(self,nombre,fecha):
        self.nombre = nombre
        self.fecha = fecha
        self.bandas = {}

    def iscribir_bandas(self):
        pass

