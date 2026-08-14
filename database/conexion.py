"""
=========================================================
Archivo:
conexion.py

Ubicación:
database/

Responsabilidad:
Administrar la conexión con SQLite.
=========================================================
"""


import sqlite3

from config.constantes import DATABASE_PATH, DATABASE_TIMEOUT


class ConexionBD:


    def __init__(self):

        self.conexion = None





    def abrir_conexion(self):
        """
        Crea y retorna una conexión SQLite.
        """


        try:


            self.conexion = sqlite3.connect(
                DATABASE_PATH,
                timeout=DATABASE_TIMEOUT
            )


            # Permite usar columnas por nombre
            self.conexion.row_factory = sqlite3.Row



            return self.conexion



        except sqlite3.Error as error:


            print(
                f"Error al conectar SQLite: {error}"
            )


            return None






    def cerrar_conexion(self):
        """
        Cierra la conexión activa.
        """


        try:


            if self.conexion:


                self.conexion.close()



        except sqlite3.Error as error:


            print(
                f"Error cerrando conexión: {error}"
            )