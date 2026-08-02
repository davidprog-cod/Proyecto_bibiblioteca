"""
=========================================================
Archivo:
views/login.py

Responsabilidad:
Ventana de inicio de sesión.

Arquitectura:
MVC - Capa Vista
=========================================================
"""


import tkinter as tk
from tkinter import messagebox

from controllers.usuario_controller import UsuarioController



class Login:


    def __init__(self, ventana):

        self.ventana = ventana


        self.ventana.title(
            "Sistema de Gestión Bibliotecaria"
        )


        self.ventana.geometry(
            "400x300"
        )


        self.ventana.resizable(
            False,
            False
        )
        self.ventana.iconbitmap(
        "assets/biblioteca.ico"
        )

        self.controlador = UsuarioController()


        self.crear_interfaz()



    # =====================================================
    # CREAR INTERFAZ
    # =====================================================

    def crear_interfaz(self):


        titulo = tk.Label(
            self.ventana,
            text="Inicio de Sesión",
            font=("Arial",18)
        )


        titulo.pack(
            pady=20
        )



        tk.Label(
            self.ventana,
            text="Usuario:"
        ).pack()



        self.usuario = tk.Entry(
            self.ventana
        )


        self.usuario.pack()



        tk.Label(
            self.ventana,
            text="Contraseña:"
        ).pack()



        self.password = tk.Entry(
            self.ventana,
            show="*"
        )


        self.password.pack()



        boton = tk.Button(
            self.ventana,
            text="Ingresar",
            width=15,
            command=self.iniciar_sesion
        )


        boton.pack(
            pady=20
        )



    # =====================================================
    # VALIDAR LOGIN
    # =====================================================

    def iniciar_sesion(self):


        nombre = self.usuario.get()

        password = self.password.get()



        resultado = self.controlador.login(
            nombre,
            password
        )



        if resultado:


            messagebox.showinfo(
                "Acceso correcto",
                "Bienvenido al sistema"
            )


            self.ventana.destroy()



            # Abrir menú principal

            from views.menu_principal import MenuPrincipal


            nueva_ventana = tk.Tk()


            MenuPrincipal(
                nueva_ventana
            )


            nueva_ventana.mainloop()



        else:


            messagebox.showerror(
                "Error",
                "Usuario o contraseña incorrectos"
            )



    # =====================================================
    # MOSTRAR VENTANA
    # =====================================================

    def mostrar(self):

        self.ventana.mainloop()