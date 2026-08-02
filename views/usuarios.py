"""
=========================================================
Archivo:
views/usuarios.py

Responsabilidad:
Interfaz gráfica del módulo Gestión de Usuarios Biblioteca.

Arquitectura:
MVC
=========================================================
"""


import tkinter as tk

from tkinter import ttk, messagebox

from controllers.persona_controller import PersonaController



class Usuarios:


    def __init__(self, ventana):


        self.ventana = ventana


        self.ventana.title(
            "Gestión de Usuarios"
        )


        self.ventana.geometry(
            "950x600"
        )


        try:

            self.ventana.iconbitmap(
            "assets/biblioteca.ico"
        )

        except:

            pass



        self.controlador = PersonaController()



        self.crear_formulario()

        self.crear_botones()

        self.crear_tabla()

        self.cargar_usuarios()



    # =====================================================
    # FORMULARIO
    # =====================================================

    def crear_formulario(self):


        frame = tk.Frame(
            self.ventana
        )

        frame.pack(
            pady=10
        )



        etiquetas = [

            "Código",
            "Cédula",
            "Nombre",
            "Apellido",
            "Teléfono",
            "Correo",
            "Dirección"

        ]


        self.campos = {}



        for i, etiqueta in enumerate(etiquetas):


            tk.Label(

                frame,

                text=etiqueta

            ).grid(

                row=i,

                column=0,

                padx=10,

                pady=5

            )


            entrada = tk.Entry(

                frame,

                width=35

            )


            entrada.grid(

                row=i,

                column=1

            )


            self.campos[etiqueta] = entrada



    # =====================================================
    # BOTONES
    # =====================================================

    def crear_botones(self):


        frame = tk.Frame(
            self.ventana
        )

        frame.pack(
            pady=10
        )


        botones = [

            ("Nuevo", self.nuevo),

            ("Guardar", self.guardar),

            ("Actualizar", self.actualizar),

            ("Buscar", self.buscar),

            ("Cancelar", self.nuevo),

            ("Eliminar", self.eliminar),

            ("Volver", self.cerrar)

        ]



        for i, boton in enumerate(botones):


            tk.Button(

                frame,

                text=boton[0],

                width=12,

                command=boton[1]

            ).grid(

                row=0,

                column=i,

                padx=5

            )



    # =====================================================
    # TABLA
    # =====================================================

    def crear_tabla(self):


        columnas = (

            "Código",

            "Cédula",

            "Nombre",

            "Apellido",

            "Teléfono",

            "Correo"

        )


        self.tabla = ttk.Treeview(

            self.ventana,

            columns=columnas,

            show="headings"

        )



        for columna in columnas:


            self.tabla.heading(

                columna,

                text=columna

            )


            self.tabla.column(

                columna,

                width=140

            )



        self.tabla.pack(

            fill="both",

            expand=True

        )



        self.tabla.bind(

            "<<TreeviewSelect>>",

            self.seleccionar

        )



    # =====================================================
    # OBTENER DATOS
    # =====================================================

    def obtener_datos(self):


        return (

            self.campos["Código"].get(),

            self.campos["Cédula"].get(),

            self.campos["Nombre"].get(),

            self.campos["Apellido"].get(),

            self.campos["Teléfono"].get(),

            self.campos["Correo"].get(),

            self.campos["Dirección"].get()

        )



    # =====================================================
    # GUARDAR
    # =====================================================

    def guardar(self):


        try:

            self.controlador.guardar(

                self.obtener_datos()

            )


            messagebox.showinfo(

                "Éxito",

                "Usuario guardado correctamente"

            )


            self.cargar_usuarios()


        except Exception as error:


            messagebox.showerror(

                "Error",

                str(error)

            )



    # =====================================================
    # CARGAR TABLA
    # =====================================================

    def cargar_usuarios(self):


        for fila in self.tabla.get_children():

            self.tabla.delete(fila)



        usuarios = self.controlador.listar()



        for usuario in usuarios:


            self.tabla.insert(

                "",

                "end",

                values=(

                    usuario[1],

                    usuario[2],

                    usuario[3],

                    usuario[4],

                    usuario[5],

                    usuario[6]

                )

            )



    # =====================================================
    # SELECCIONAR
    # =====================================================

    def seleccionar(self,event):


        seleccionado = self.tabla.selection()


        if seleccionado:


            datos = self.tabla.item(

                seleccionado

            )


            valores = datos["values"]



            campos = [

                "Código",

                "Cédula",

                "Nombre",

                "Apellido",

                "Teléfono",

                "Correo"

            ]



            for i,campo in enumerate(campos):


                self.campos[campo].delete(

                    0,

                    "end"

                )


                self.campos[campo].insert(

                    0,

                    valores[i]

                )



    # =====================================================
    # BUSCAR
    # =====================================================

    def buscar(self):


        texto = self.campos["Nombre"].get()



        resultados = self.controlador.buscar(

            texto

        )



        for fila in self.tabla.get_children():

            self.tabla.delete(fila)



        for usuario in resultados:


            self.tabla.insert(

                "",

                "end",

                values=(

                    usuario[1],

                    usuario[2],

                    usuario[3],

                    usuario[4],

                    usuario[5],

                    usuario[6]

                )

            )



    # =====================================================
    # ACTUALIZAR
    # =====================================================

    def actualizar(self):


        messagebox.showinfo(

            "Información",

            "Actualización pendiente"

        )



    # =====================================================
    # ELIMINAR
    # =====================================================

    def eliminar(self):


        messagebox.showinfo(

            "Información",

            "Eliminación pendiente"

        )



    # =====================================================
    # LIMPIAR CAMPOS
    # =====================================================

    def nuevo(self):


        for campo in self.campos.values():


            campo.delete(

                0,

                "end"

            )



    # =====================================================
    # CERRAR VENTANA
    # =====================================================

    def cerrar(self):


        self.ventana.destroy()