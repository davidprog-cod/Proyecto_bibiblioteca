"""
=========================================================
Archivo: login.py

Ubicación:
Proyecto_biblioteca/views/

Descripción:
Ventana inicial de acceso al sistema.

Actualmente funciona como pantalla inicial.
Posteriormente se conectará con usuarios y roles.
=========================================================
"""


import tkinter as tk

from tkinter import messagebox

from views.menu import MenuPrincipal





class Login:

    """
    Ventana de inicio de sesión.
    """



    def __init__(self, ventana):

        self.ventana = ventana

        self.ventana.title(
            "Login - Biblioteca"
        )

        self.ventana.geometry(
            "400x300"
        )


        self.crear_interfaz()



    def crear_interfaz(self):


        titulo = tk.Label(
            self.ventana,
            text="Sistema de Gestión Bibliotecaria",
            font=("Arial",14,"bold")
        )

        titulo.pack(
            pady=20
        )



        tk.Label(
            self.ventana,
            text="Usuario"
        ).pack()



        self.usuario = tk.Entry(
            self.ventana
        )

        self.usuario.pack()



        tk.Label(
            self.ventana,
            text="Contraseña"
        ).pack()



        self.password = tk.Entry(
            self.ventana,
            show="*"
        )

        self.password.pack()



        boton = tk.Button(
            self.ventana,
            text="Ingresar",
            command=self.ingresar
        )

        boton.pack(
            pady=20
        )





    def ingresar(self):

        """
        Acceso temporal.

        Posteriormente se validará
        contra usuarios y roles.
        """

        if self.usuario.get():


            self.ventana.destroy()


            nueva = tk.Tk()

            MenuPrincipal(nueva)


            nueva.mainloop()



        else:

            messagebox.showwarning(
                "Aviso",
                "Ingrese usuario"
            )