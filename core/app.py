"""
=========================================================
Archivo:
app.py

Ubicación:
core/

Responsabilidad:
Inicializar la aplicación Tkinter.
=========================================================
"""


import tkinter as tk


from database.crear_bd import CrearBD

from views.login import Login





class Aplicacion:


    def __init__(self):


        # Crear base de datos
        self.crear_base_datos()


        # Crear ventana principal
        self.ventana = tk.Tk()


        self.ventana.title(
            "Sistema de Gestión Bibliotecaria"
        )


        self.ventana.geometry(
            "400x300"
        )



        # Abrir login
        Login(
            self.ventana
        )





    def crear_base_datos(self):


        creador = CrearBD()

        creador.crear_tablas()





    def ejecutar(self):


        # Mantiene abierta la ventana

        self.ventana.mainloop()