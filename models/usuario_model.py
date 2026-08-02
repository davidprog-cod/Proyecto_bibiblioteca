"""
=========================================================
Archivo:
usuario_model.py

Ubicación:
Proyecto_biblioteca/models/

Responsabilidad:
Gestionar únicamente operaciones SQL
de la tabla usuarios.
=========================================================
"""


import sqlite3

from database.conexion import ConexionBD




class UsuarioModel:


    def __init__(self):

        self.conexion_bd = ConexionBD()



    def insertar_usuario(self, usuario):


        conexion = self.conexion_bd.abrir_conexion()


        if conexion is None:

            return False



        try:


            cursor = conexion.cursor()



            cursor.execute(
                """
                INSERT INTO usuarios
                (
                    cedula,
                    nombres,
                    apellidos,
                    correo,
                    telefono,
                    direccion
                )

                VALUES(?,?,?,?,?,?)

                """,

                (
                    usuario["cedula"],
                    usuario["nombres"],
                    usuario["apellidos"],
                    usuario["correo"],
                    usuario["telefono"],
                    usuario["direccion"]
                )
            )


            conexion.commit()


            return True



        except sqlite3.Error as error:


            print(
                f"Error insertando usuario: {error}"
            )


            return False



        finally:

            self.conexion_bd.cerrar_conexion()





    def actualizar_usuario(
            self,
            id_usuario,
            usuario
    ):


        conexion = self.conexion_bd.abrir_conexion()


        if conexion is None:

            return False



        try:


            cursor = conexion.cursor()



            cursor.execute(
                """
                UPDATE usuarios

                SET

                nombres=?,
                apellidos=?,
                correo=?,
                telefono=?,
                direccion=?

                WHERE id=?

                """,

                (

                    usuario["nombres"],
                    usuario["apellidos"],
                    usuario["correo"],
                    usuario["telefono"],
                    usuario["direccion"],
                    id_usuario

                )

            )



            conexion.commit()



            return cursor.rowcount > 0



        except sqlite3.Error as error:


            print(error)


            return False



        finally:


            self.conexion_bd.cerrar_conexion()






    def eliminar_usuario(
            self,
            id_usuario
    ):


        conexion = self.conexion_bd.abrir_conexion()


        if conexion is None:

            return False



        try:


            cursor = conexion.cursor()



            cursor.execute(
                """
                DELETE FROM usuarios
                WHERE id=?
                """,

                (
                    id_usuario,
                )

            )



            conexion.commit()



            return cursor.rowcount > 0



        except sqlite3.Error as error:


            print(error)


            return False



        finally:

            self.conexion_bd.cerrar_conexion()






    def obtener_usuarios(self):


        conexion = self.conexion_bd.abrir_conexion()


        if conexion is None:

            return []



        try:


            cursor = conexion.cursor()



            cursor.execute(
                """
                SELECT *

                FROM usuarios

                ORDER BY id DESC

                """
            )


            return cursor.fetchall()



        except sqlite3.Error as error:


            print(error)


            return []



        finally:

            self.conexion_bd.cerrar_conexion()





    def buscar_usuario(
            self,
            criterio,
            valor
    ):


        conexion = self.conexion_bd.abrir_conexion()


        if conexion is None:

            return []



        try:


            cursor = conexion.cursor()



            if criterio=="nombre":


                cursor.execute(
                    """
                    SELECT *

                    FROM usuarios

                    WHERE nombres LIKE ?

                    """,

                    (
                        f"%{valor}%",
                    )

                )



            elif criterio=="cedula":


                cursor.execute(
                    """
                    SELECT *

                    FROM usuarios

                    WHERE cedula LIKE ?

                    """,

                    (
                        f"%{valor}%",
                    )

                )



            return cursor.fetchall()



        except sqlite3.Error as error:


            print(error)


            return []



        finally:

            self.conexion_bd.cerrar_conexion()