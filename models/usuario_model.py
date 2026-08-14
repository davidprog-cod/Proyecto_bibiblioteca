"""
=========================================================
Archivo:
models/usuario_model.py

Responsabilidad:
Gestionar todas las operaciones relacionadas
con los usuarios usando SQLite.

Arquitectura:
MVC - Capa Modelo
=========================================================
"""


import sqlite3


class UsuarioModel:


    def __init__(self):

        self.ruta_bd = "database/biblioteca.db"



    # =====================================================
    # CONEXIÓN A BASE DE DATOS
    # =====================================================

    def conectar(self):

        return sqlite3.connect(self.ruta_bd)



    # =====================================================
    # BUSCAR USUARIO PARA LOGIN
    # =====================================================

    def validar_usuario(self, nombre, password):

        conexion = self.conectar()

        cursor = conexion.cursor()


        cursor.execute(
            """
            SELECT id, nombre, rol
            FROM usuarios
            WHERE nombre = ?
            AND password = ?
            """,
            (nombre, password)
        )


        usuario = cursor.fetchone()


        conexion.close()


        return usuario



    # =====================================================
    # REGISTRAR USUARIO
    # =====================================================

    def registrar_usuario(self, nombre, password, rol):

        conexion = self.conectar()

        cursor = conexion.cursor()


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
                nombre,
                password,
                rol
            )
        )


        conexion.commit()

        conexion.close()



    # =====================================================
    # OBTENER TODOS LOS USUARIOS
    # =====================================================

    def obtener_usuarios(self):

        conexion = self.conectar()

        cursor = conexion.cursor()


        cursor.execute(
            """
            SELECT id, nombre, rol
            FROM usuarios
            """
        )


        usuarios = cursor.fetchall()


        conexion.close()


        return usuarios



    # =====================================================
    # ELIMINAR USUARIO
    # =====================================================

    def eliminar_usuario(self, id_usuario):

        conexion = self.conectar()

        cursor = conexion.cursor()


        cursor.execute(
            """
            DELETE FROM usuarios
            WHERE id = ?
            """,
            (id_usuario,)
        )


        conexion.commit()

        conexion.close()



    # =====================================================
    # ACTUALIZAR USUARIO
    # =====================================================

    def actualizar_usuario(
            self,
            id_usuario,
            nombre,
            password,
            rol
        ):


        conexion = self.conectar()

        cursor = conexion.cursor()


        cursor.execute(
            """
            UPDATE usuarios
            SET nombre = ?,
                password = ?,
                rol = ?

            WHERE id = ?
            """,
            (
                nombre,
                password,
                rol,
                id_usuario
            )
        )


        conexion.commit()

        conexion.close()
