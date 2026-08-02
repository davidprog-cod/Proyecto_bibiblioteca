"""
=========================================================
Archivo: usuarios.py

Ubicación:
Proyecto_biblioteca/views/

Descripción:
Interfaz gráfica del módulo Usuarios.

No contiene:
- SQL
- Consultas
- Reglas de negocio

Todo se comunica mediante UsuarioController.
=========================================================
"""


import tkinter as tk


from tkinter import ttk, messagebox


from controllers.usuario_controller import UsuarioController





class Usuarios:


    def __init__(self, ventana):


        self.ventana = ventana


        self.ventana.title(
            "Gestión de Usuarios"
        )


        self.ventana.geometry(
            "950x600"
        )

        self.ventana.iconbitmap(
            "assets/images (1).ico"
        )

        self.controlador = UsuarioController()


        self.id_usuario = None


        self.crear_formulario()


        self.crear_tabla()


        self.cargar_usuarios()





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



        for i, texto in enumerate(etiquetas):


            tk.Label(
                frame,
                text=texto
            ).grid(
                row=i,
                column=0,
                padx=5,
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


            self.campos[texto] = entrada





        botones = tk.Frame(
            self.ventana
        )


        botones.pack(
            pady=10
        )



        tk.Button(
            botones,
            text="Nuevo",
            command=self.nuevo
        ).grid(
            row=0,
            column=0,
            padx=5
        )



        tk.Button(
            botones,
            text="Guardar",
            command=self.guardar
        ).grid(
            row=0,
            column=1,
            padx=5
        )



        tk.Button(
            botones,
            text="Actualizar",
            command=self.actualizar
        ).grid(
            row=0,
            column=2,
            padx=5
        )



        tk.Button(
            botones,
            text="Buscar",
            command=self.buscar
        ).grid(
            row=0,
            column=3,
            padx=5
        )



        tk.Button(
            botones,
            text="Cancelar",
            command=self.nuevo
        ).grid(
            row=0,
            column=4,
            padx=5
        )

        tk.Button(
        botones,
        text="Eliminar",
        command=self.eliminar
        ).grid(
            row=0,
            column=5,
            padx=5
        )




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
                width=120
            )



        self.tabla.pack(
            fill="both",
            expand=True
        )


        self.tabla.bind(
            "<<TreeviewSelect>>",
            self.seleccionar
        )





    def obtener_datos(self):


        return {

            "cedula":
            self.campos["Cédula"].get(),

            "nombres":
            self.campos["Nombre"].get(),

            "apellidos":
            self.campos["Apellido"].get(),

            "telefono":
            self.campos["Teléfono"].get(),

            "correo":
            self.campos["Correo"].get(),

            "direccion":
            self.campos["Dirección"].get()

        }





    def guardar(self):


        respuesta = self.controlador.registrar_usuario(
            self.obtener_datos()
        )


        messagebox.showinfo(
            "Resultado",
            respuesta["mensaje"]
        )


        self.cargar_usuarios()





    def actualizar(self):


        if self.id_usuario is None:

            messagebox.showwarning(
                "Aviso",
                "Seleccione un usuario"
            )

            return



        respuesta = self.controlador.actualizar_usuario(
            self.id_usuario,
            self.obtener_datos()
        )


        messagebox.showinfo(
            "Resultado",
            respuesta["mensaje"]
        )


        self.cargar_usuarios()





    def cargar_usuarios(self):


        for fila in self.tabla.get_children():

            self.tabla.delete(fila)



        usuarios = self.controlador.listar_usuarios()



        for usuario in usuarios:


            self.tabla.insert(

                "",

                "end",

                values=(

                    usuario["id"],
                    usuario["cedula"],
                    usuario["nombres"],
                    usuario["apellidos"],
                    usuario["telefono"],
                    usuario["correo"]

                )

            )





    def seleccionar(self,event):


        seleccionado = self.tabla.selection()



        if seleccionado:


            datos = self.tabla.item(
                seleccionado
            )


            valores = datos["values"]


            self.id_usuario = valores[0]


            self.campos["Código"].delete(0,"end")

            self.campos["Código"].insert(
                0,
                valores[0]
            )


            self.campos["Cédula"].delete(0,"end")

            self.campos["Cédula"].insert(
                0,
                valores[1]
            )


            self.campos["Nombre"].delete(0,"end")

            self.campos["Nombre"].insert(
                0,
                valores[2]
            )


            self.campos["Apellido"].delete(0,"end")

            self.campos["Apellido"].insert(
                0,
                valores[3]
            )


            self.campos["Teléfono"].delete(0,"end")

            self.campos["Teléfono"].insert(
                0,
                valores[4]
            )


            self.campos["Correo"].delete(0,"end")

            self.campos["Correo"].insert(
                0,
                valores[5]
            )





    def buscar(self):


        texto = self.campos["Nombre"].get()



        resultados = self.controlador.buscar_usuario(
            "nombre",
            texto
        )



        for fila in self.tabla.get_children():

            self.tabla.delete(fila)



        for usuario in resultados:


            self.tabla.insert(

                "",

                "end",

                values=(

                    usuario["id"],
                    usuario["cedula"],
                    usuario["nombres"],
                    usuario["apellidos"],
                    usuario["telefono"],
                    usuario["correo"]

                )

            )





    def nuevo(self):


        self.id_usuario = None


        for campo in self.campos.values():

            campo.delete(
                0,
                "end"
            )