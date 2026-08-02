"""
=========================================================
Archivo:
usuario_controller.py

Ubicación:
controllers/

Responsabilidad:
Controlar reglas del módulo usuarios.
=========================================================
"""


from models.usuario_model import UsuarioModel

from utils.validaciones import (
    validar_campo_vacio,
    validar_correo,
    validar_cedula
)




class UsuarioController:



    def __init__(self):

        self.modelo = UsuarioModel()



    def registrar_usuario(
            self,
            datos
    ):


        if validar_campo_vacio(datos["cedula"]):

            return {
                "mensaje":
                "La cédula es obligatoria"
            }



        if not validar_cedula(
            datos["cedula"]
        ):

            return {
                "mensaje":
                "Cédula incorrecta"
            }



        if datos["correo"]:

            if not validar_correo(
                datos["correo"]
            ):

                return {
                    "mensaje":
                    "Correo inválido"
                }



        resultado = self.modelo.insertar_usuario(
            datos
        )


        if resultado:

            return {
                "mensaje":
                "Usuario registrado correctamente"
            }



        return {
            "mensaje":
            "Error al registrar usuario"
        }





    def actualizar_usuario(
            self,
            id_usuario,
            datos
    ):


        resultado = self.modelo.actualizar_usuario(
            id_usuario,
            datos
        )


        if resultado:

            return {
                "mensaje":
                "Usuario actualizado"
            }



        return {
            "mensaje":
            "No se pudo actualizar"
        }





    def eliminar_usuario(
            self,
            id_usuario
    ):


        resultado = self.modelo.eliminar_usuario(
            id_usuario
        )


        if resultado:

            return {
                "mensaje":
                "Usuario eliminado"
            }



        return {
            "mensaje":
            "No encontrado"
        }





    def listar_usuarios(self):

        return self.modelo.obtener_usuarios()





    def buscar_usuario(
            self,
            criterio,
            valor
    ):

        return self.modelo.buscar_usuario(
            criterio,
            valor
        )