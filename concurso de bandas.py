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
        else:
            self._categoria = categoria

    def registrar_puntajes(self,puntajes):
        for criterio in self.Criterios:
            if criterio not in puntajes:
                raise ValueError(f"Falta criterio: {criterio}")
            if not (0 <= puntajes[criterio] <= 10):
                raise ValueError(f"Puntaje inválido para {criterio}, debe ser de 0 a 10")
        self._puntaje = sum(puntajes.values())


    def mostrar_info(self):
        if self._puntaje:
            return f"Nombre: {self.nombre}-Institucion: {self.institucion} - Categoría: {self._categoria} - Puntaje total: {self.total} - Puntaje promedio: {self.promedio:.2f}"
        else:
            return f"Nombre: {self.nombre}-Insitucion: {self.institucion} - Categoría: {self._categoria}"

class Concurso:
    def __init__(self,nombre,fehca):
        self.nombre = nombre
        self.fecha = fehca
        self.bandas = {}

    def InscribirBandas(self,banda):
        if banda.nombre in self.bandas:
            raise ValueError(f"La banda {banda.nombre} ya existe.")
        else:
            self.bandas[banda.nombre] = banda

    def registrar_Evaluacion(self,nombre_banda,puntajes):
        if nombre_banda not in self.bandas:
            raise ValueError(f"La banda {nombre_banda} no esta inscrita.")
        else:
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

        dato = "----Ranking----\n"
        posicion = 1
        for banda in bandas_lista:
            dato += f"Posicion: {banda.nombre}-{banda.institucion}-{banda.categoria}-Total: {banda.total}\n"
            posicion += 1
        return dato

class ConcursoBandasApp:
        def __init__(self):
            self.ventana = tk.Tk()
            self.ventana.title("Concurso de Bandas - Quetzaltenango")
            self.ventana.geometry("500x300")

            self.concurso_obj = Concurso("Concurso de Bandas - 14 de Septiembre", "2025-09-14")

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
            ventana_inscribir= tk.Toplevel(self.ventana)
            ventana_inscribir.title("Inscribir Banda")

            tk.Label(ventana_inscribir, text="Ingrese el nombre de la banda: ").pack(pady=5)
            entrada1 = tk.Entry(ventana_inscribir)
            entrada1.pack(pady=5)

            tk.Label(ventana_inscribir, text="Ingrese la institución de la banda: ").pack(pady=5)
            entrada2 = tk.Entry(ventana_inscribir)
            entrada2.pack(pady=5)

            tk.Label(ventana_inscribir, text="Ingrese la categoría (Primaria, Basico, Diversificado):").pack(pady=5)
            entrada3 = tk.Entry(ventana_inscribir)
            entrada3.pack(pady=5)

            def guardar_datos():
                nombre=entrada1.get().lower()
                institucion=entrada2.get()
                categoria=entrada3.get()

                try:
                    banda=BandasEscolar(nombre,institucion,categoria, None)
                    self.concurso_obj.InscribirBandas(banda)
                    print(f"Banda {nombre} inscrita exitosamente.")

                except Exception as e:
                    print(e)

            tk.Button(ventana_inscribir, text="Guardar", command=guardar_datos).pack(pady=5)


        def registrar_evaluacion(self):
            print("Se abrió la ventana: Registrar Evaluación")
            ventana_registrar = tk.Toplevel(self.ventana)
            ventana_registrar.title("Registrar Evaluacion")

            tk.Label(ventana_registrar, text="Ingrese el nombre de la banda a calificar: ").pack(pady=5)
            entrada1 = tk.Entry(ventana_registrar)
            entrada1.pack(pady=5)

            def buscar_banda():
                nombre_buscar = (entrada1.get()).lower()

                if nombre_buscar in self.concurso_obj.bandas:
                    etiqueta1 = (tk.Label(ventana_registrar, text=f"Banda {nombre_buscar} encontrada."))
                    etiqueta1.pack(pady=5)

                    registros_puntajes={}

                    for criterio in BandasEscolar.Criterios:
                        tk.Label(ventana_registrar, text=f"{criterio} (0-10)").pack(pady=5)
                        entrada=tk.Entry(ventana_registrar)
                        entrada.pack()
                        registros_puntajes[criterio]= entrada

                    def guardar_evaluacion():
                        try:
                            puntajes = {c: int(e.get()) for c, e in registros_puntajes.items()} #Investigue que asi se hace mejor
                            self.concurso_obj.registrar_Evaluacion(nombre_buscar, puntajes)
                            tk.Label(ventana_registrar, text="Puntaje registrado exitosamente").pack(pady=5)

                        except Exception as e:
                            tk.Label(ventana_registrar, text=f"Error: {e}").pack(pady=5)

                    tk.Button(ventana_registrar, text="Guardad puntajes", command=guardar_evaluacion).pack(pady=5)

                else:
                    etiqueta1=(tk.Label(ventana_registrar, text="Banda no encontrada"))
                    etiqueta1.pack(pady=5)

            tk.Button(ventana_registrar, text="Buscar", command=buscar_banda).pack(pady=5)


        def listar_bandas(self):
            print("Se abrió la ventana: Listado de Bandas")
            ventana_lista = tk.Toplevel(self.ventana)
            ventana_lista.title("Listado de Bandas")

            texto = tk.Text(ventana_lista, width=100, height=20)
            texto.pack(pady=5)
            texto.pack(padx=5, pady=5)
            texto.insert("1.0", self.concurso_obj.listar_bandas())

        def ver_ranking(self):
            print("Se abrió la ventana: Ranking de bandas")
            ventana_rank = tk.Toplevel(self.ventana)
            ventana_rank.title("Mostrar de Bandas")

            texto = tk.Text(ventana_rank, width=100, height=20)
            texto.pack(pady=5)
            texto.pack(padx=10, pady=10)
            texto.insert("1.0", self.concurso_obj.ranking())

if __name__ == "__main__":
        ConcursoBandasApp()












