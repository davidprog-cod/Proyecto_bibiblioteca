"""
=========================================================
Archivo:
crear_bd.py

Ubicación:
database/

Responsabilidad:
Crear automáticamente la base de datos
y las tablas iniciales.
=========================================================
"""


import sqlite3


from database.conexion import ConexionBD





class CrearBD:


    def __init__(self):

        self.conexion = ConexionBD()





    def crear_tablas(self):


        conexion = self.conexion.abrir_conexion()



        if conexion is None:

            return



        try:


            cursor = conexion.cursor()



            cursor.execute(
                """

                CREATE TABLE IF NOT EXISTS usuarios(

                    id INTEGER PRIMARY KEY AUTOINCREMENT,

                    cedula TEXT NOT NULL UNIQUE,

                    nombres TEXT NOT NULL,

                    apellidos TEXT NOT NULL,

                    telefono TEXT,

                    correo TEXT,

                    direccion TEXT,

                    fecha_registro 
                    TIMESTAMP DEFAULT CURRENT_TIMESTAMP

                );

                """
            )



            conexion.commit()



            print(
                "======================================"
            )

            print(
                "Base de datos creada correctamente."
            )

            print(
                "Tabla usuarios creada correctamente."
            )

            print(
                "======================================"
            )



        except sqlite3.Error as error:


            print(
                f"Error creando base de datos: {error}"
            )



        finally:


            self.conexion.cerrar_conexion()