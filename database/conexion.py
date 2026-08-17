"""
=========================================================
Archivo:
conexion.py

Ubicacion:
database/

Responsabilidad:
Administrar la conexion con SQLite.
=========================================================
"""


import sqlite3

from config.constantes import DATABASE_PATH, DATABASE_TIMEOUT


class ConexionBD:


    def __init__(self):

        self.conexion = None


    def abrir_conexion(self):
        """Crea y retorna una conexion SQLite."""

        try:

            self.conexion = sqlite3.connect(
                DATABASE_PATH,
                timeout=DATABASE_TIMEOUT
            )

            self.conexion.row_factory = sqlite3.Row

            return self.conexion

        except sqlite3.Error:

            return None


    def cerrar_conexion(self):
        """Cierra la conexion activa."""

        try:

            if self.conexion:

                self.conexion.close()

        except sqlite3.Error:

            pass
