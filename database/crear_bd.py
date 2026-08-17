"""
=========================================================
Archivo:
database/crear_bd.py

Responsabilidad:
Crear y preparar la base de datos SQLite.

Arquitectura:
MVC - Capa Database
=========================================================
"""


import sqlite3


class CrearBD:


    def __init__(self):

        self.ruta_bd = "database/biblioteca.db"


    def crear_tablas(self):

        conexion = sqlite3.connect(self.ruta_bd)

        cursor = conexion.cursor()


        # =================================================
        # TABLA USUARIOS
        # =================================================

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS usuarios(

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                nombre TEXT NOT NULL UNIQUE,

                password TEXT NOT NULL,

                rol TEXT NOT NULL

            )
            """
        )


        # =================================================
        # CREAR ADMINISTRADOR INICIAL
        # =================================================

        cursor.execute(
            """
            SELECT *
            FROM usuarios
            WHERE nombre = ?
            """,
            ("admin",)
        )

        usuario = cursor.fetchone()

        if usuario is None:

            cursor.execute(
                """
                INSERT INTO usuarios
                (
                    nombre,
                    password,
                    rol
                )
                VALUES (?, ?, ?)
                """,
                (
                    "admin",
                    "1234",
                    "Administrador"
                )
            )


        # =================================================
        # TABLA PERSONAS
        # =================================================

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS personas (

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                codigo TEXT UNIQUE NOT NULL,

                cedula TEXT UNIQUE NOT NULL,

                nombre TEXT NOT NULL,

                apellido TEXT NOT NULL,

                telefono TEXT,

                correo TEXT,

                direccion TEXT

            )
            """
        )


        # =================================================
        # TABLA LIBROS
        # =================================================

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS libros (

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                isbn TEXT UNIQUE NOT NULL,

                titulo TEXT NOT NULL,

                autor TEXT NOT NULL,

                editorial TEXT,

                anio INTEGER,

                categoria TEXT NOT NULL,

                cantidad INTEGER NOT NULL DEFAULT 0,

                disponible INTEGER NOT NULL DEFAULT 1

            )
            """
        )


        conexion.commit()

        conexion.close()
