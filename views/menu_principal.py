"""
=========================================================
Archivo:
views/menu_principal.py

Responsabilidad:
Menú principal del sistema bibliotecario.

Arquitectura:
MVC - Capa Vista
=========================================================
"""


import tkinter as tk


from views.usuarios import Usuarios



class MenuPrincipal:


    def __init__(self, ventana):


        self.ventana = ventana


        self.ventana.title(
            "Sistema de Gestión Bibliotecaria"
        )


        self.ventana.geometry(
            "600x400"
        )


        self.ventana.resizable(
            False,
            False
        )

        self.ventana.iconbitmap(
        "assets/biblioteca.ico"
        )
        try:

            self.ventana.iconbitmap(
                "assets/images (1).ico"
            )

        except:

            pass



        self.crear_interfaz()



    # =====================================================
    # INTERFAZ DEL MENU
    # =====================================================

    def crear_interfaz(self):


        titulo = tk.Label(

            self.ventana,

            text="Sistema de Biblioteca",

            font=("Arial", 18, "bold")

        )


        titulo.pack(

            pady=40

        )



        boton_usuarios = tk.Button(

            self.ventana,

            text="Gestión de Usuarios",

            width=30,

            height=2,

            command=self.abrir_usuarios

        )


        boton_usuarios.pack(

            pady=10

        )



        boton_cerrar = tk.Button(

            self.ventana,

            text="Cerrar Sesión",

            width=30,

            height=2,

            command=self.cerrar_sesion

        )


        boton_cerrar.pack(

            pady=10

        )



    # =====================================================
    # ABRIR GESTION USUARIOS
    # =====================================================

    def abrir_usuarios(self):


        ventana_usuario = tk.Toplevel(

            self.ventana

        )


        Usuarios(

            ventana_usuario

        )



    # =====================================================
    # CERRAR SESION
    # =====================================================

    def cerrar_sesion(self):


        self.ventana.destroy()



        nueva_ventana = tk.Tk()


        from views.login import Login


        Login(

            nueva_ventana

        )


        nueva_ventana.mainloop()