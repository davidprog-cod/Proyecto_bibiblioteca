"""
=========================================================
Archivo:
models/persona_model.py

Responsabilidad:
Gestionar usuarios de biblioteca usando SQLite.

Arquitectura:
MVC - Capa Modelo
=========================================================
"""


import sqlite3



class PersonaModel:


    def __init__(self):

        self.ruta_bd = "database/biblioteca.db"



    # =====================================================
    # CONEXIÓN
    # =====================================================

    def conectar(self):

        return sqlite3.connect(
            self.ruta_bd
        )



    # =====================================================
    # REGISTRAR PERSONA
    # =====================================================

    def guardar_persona(self, datos):

        conexion = self.conectar()

        cursor = conexion.cursor()


        cursor.execute(
            """
            INSERT INTO personas
            (
                codigo,
                cedula,
                nombre,
                apellido,
                telefono,
                correo,
                direccion
            )

            VALUES (?, ?, ?, ?, ?, ?, ?)

            """,
            datos
        )


        conexion.commit()

        conexion.close()



    # =====================================================
    # MOSTRAR PERSONAS
    # =====================================================

    def obtener_personas(self):

        conexion = self.conectar()

        cursor = conexion.cursor()


        cursor.execute(
            """
            SELECT
            id,
            codigo,
            cedula,
            nombre,
            apellido,
            telefono,
            correo,
            direccion

            FROM personas
            """
        )


        personas = cursor.fetchall()


        conexion.close()


        return personas



    # =====================================================
    # BUSCAR PERSONA
    # =====================================================

    def buscar_persona(self, texto):

        conexion = self.conectar()

        cursor = conexion.cursor()


        cursor.execute(
            """
            SELECT *
            FROM personas

            WHERE codigo LIKE ?
            OR cedula LIKE ?
            OR nombre LIKE ?

            """,
            (
                "%" + texto + "%",
                "%" + texto + "%",
                "%" + texto + "%"
            )
        )


        resultado = cursor.fetchall()


        conexion.close()


        return resultado



    # =====================================================
    # ACTUALIZAR PERSONA
    # =====================================================

    def actualizar_persona(self, datos):

        conexion = self.conectar()

        cursor = conexion.cursor()


        cursor.execute(
            """
            UPDATE personas

            SET
            codigo=?,
            cedula=?,
            nombre=?,
            apellido=?,
            telefono=?,
            correo=?,
            direccion=?

            WHERE id=?

            """,
            datos
        )


        conexion.commit()

        conexion.close()



    # =====================================================
    # ELIMINAR PERSONA
    # =====================================================

    def eliminar_persona(self, id_persona):

        conexion = self.conectar()

        cursor = conexion.cursor()


        cursor.execute(
            """
            DELETE FROM personas

            WHERE id=?

            """,
            (id_persona,)
        )


        conexion.commit()

        conexion.close()