class participante:
    def __init__(self,nombre,institucion):
        self.nombre = nombre
        self.institucion = institucion

    def mostrar_info(self):
        return f"Nombre: {self.nombre}-Insitucion: {self.institucion}"

class BandasEscolar(participante):
    Categorias_Validas = ["Primaria","Basico","Diversificado"]
    Criterios = ["Ritmo","Uniformidad","Coreografia","Alineacion","Puntualidad"]

    def __init__(self,nombre,institucion,categoria,puntaje):
        super().__init__(nombre,institucion)
        self._categoria = categoria
        self._puntaje = puntaje
        self.registrar_puntaje = {}
    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def set_categoria(self, categoria):
        if categoria not in self.Categorias_Validas:
            raise ValueError("Categoría inválida, debe ser: Primaria, Básico o Diversificado")
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
    def __init__(self,nombre,fehca):
        self.nombre = nombre
        self.fecha = fehca
        self.bandas = {}

    def InscribirBandas(self,banda):
        if banda.nombre in self.bandas:
            raise ValueError(f"La banda {banda.nombre} ya existe.")
        self.bandas[banda.nombre] = banda

    def registrar_Evaluacion(self,nombre_banda,puntajes):
        if nombre_banda not in self.bandas:
            raise ValueError(f"La banda {nombre_banda} no esta inscrita.")
        self.bandas[nombre_banda].registrar_puntajes(puntajes)

    def listar_bandas(self):
        dato = "-- Listado de Bandas --\n"
        for banda in self.bandas.values():
            dato += banda.mostrar_info() + "\n"
        return dato










