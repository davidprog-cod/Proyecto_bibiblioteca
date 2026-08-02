"""
=========================================================
Archivo: menu.py

Ubicación:
Proyecto_biblioteca/views/

Descripción:
Menú principal del sistema.
=========================================================
"""


import tkinter as tk


from views.usuarios import Usuarios





class MenuPrincipal:


    def __init__(self, ventana):


        self.ventana = ventana


        self.ventana.title(
            "Sistema Bibliotecario"
        )


        self.ventana.geometry(
            "600x400"
        )

        self.ventana.iconbitmap(
            "assets/images (1).ico"
        )

        self.crear_menu()





    def crear_menu(self):


        titulo = tk.Label(
            self.ventana,
            text="Menú Principal",
            font=("Arial",18,"bold")
        )


        titulo.pack(
            pady=30
        )



        boton_usuario = tk.Button(
            self.ventana,
            text="Gestión Usuarios",
            width=25,
            command=self.abrir_usuarios
        )


        boton_usuario.pack(
            pady=10
        )





    def abrir_usuarios(self):


     ventana = tk.Toplevel(
         self.ventana
      )


     ventana.grab_set()


     Usuarios(
         ventana
     )