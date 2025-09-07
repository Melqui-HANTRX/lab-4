import tkinter as tk
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
    def total(self):
        return self._puntaje

    @property
    def promedio(self):
        return self._puntaje / len(self.Criterios) if self._puntaje else 0

    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, categoria):
        if categoria not in self.Categorias_Validas:
            raise ValueError("Categoría inválida, debe ser: Primaria, Básico o Diversificado".lower())
        self._categoria = categoria

    def registrar_puntajes(self,puntajes):
        for criterio in self.Criterios:
            if criterio not in puntajes:
                raise ValueError(f"Falta criterio: {criterio}")
            if not (0 <= puntajes[criterio] <= 10):
                raise ValueError(f"Puntaje inválido para {criterio}, debe ser de 0 a 10")
        self._puntaje = sum(self._puntajes.values())


    def mostrar_info(self):
        if self._puntaje:
            return f"Nombre: {self.nombre}-Institucion: {self.institucion} - Categoría: {self._categoria} - Puntaje total: {self.total} - Puntaje promedio: {self.promedio:.2f}"
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

    def ranking(self):
        bandas_lista = list(self.bandas.values())
        bandas_ct = len(bandas_lista)
        for i in range(bandas_ct):
            for j in range(0,bandas_ct-i-1):
                if bandas_lista[j].total < bandas_lista[j+1].total:
                    bandas_lista[j], bandas_lista[j+1] = bandas_lista [j+1], bandas_lista[j]

        dato = "----Ranking----"
        posicion = 1
        for banda in bandas_lista:
            dato += f"Posicion: {banda.nombre}-{banda.institucion}-{banda.categoria}-Total: {banda.total}"
            posicion += 1
        return dato

class ConcursoBandasApp:
        def __init__(self):
            self.ventana = tk.Tk()
            self.ventana.title("Concurso de Bandas - Quetzaltenango")
            self.ventana.geometry("500x300")

            self.concurso_obj = concurso("Concurso de Bandas - 14 de Septiembre", "2025-09-14")

            self.menu()

            tk.Label(
                self.ventana,
                text="Sistema de Inscripción y Evaluación de Bandas Escolares\nConcurso 14 de Septiembre - Quetzaltenango",
                font=("Arial", 12, "bold"),
                justify="center"
            ).pack(pady=50)

            self.ventana.mainloop()


        def menu(self):
            barra = tk.Menu(self.ventana)
            opciones = tk.Menu(barra, tearoff=0)
            opciones.add_command(label="Inscribir Banda", command=self.inscribir_banda)
            opciones.add_command(label="Registrar Evaluación", command=self.registrar_evaluacion)
            opciones.add_command(label="Listar Bandas", command=self.listar_bandas)
            opciones.add_command(label="Ver Ranking", command=self.ver_ranking)
            opciones.add_separator()
            opciones.add_command(label="Salir", command=self.ventana.quit)
            barra.add_cascade(label="Opciones", menu=opciones)
            self.ventana.config(menu=barra)

        def inscribir_banda(self):
            print("Se abrió la ventana: Inscribir Banda")
            tk.Toplevel(self.ventana).title("Inscribir Banda")


        def registrar_evaluacion(self):
            print("Se abrió la ventana: Registrar Evaluación")
            tk.Toplevel(self.ventana).title("Registrar Evaluación")


        def listar_bandas(self):
            print("Se abrió la ventana: Listado de Bandas")
            tk.Toplevel(self.ventana).title("Listado de Bandas")

        def ver_ranking(self):
            print("Se abrió la ventana: Ranking Final")
            tk.Toplevel(self.ventana).title("Ranking Final")

if __name__ == "__main__":
        ConcursoBandasApp()












