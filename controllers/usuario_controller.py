"""
=========================================================
Archivo:
controllers/usuario_controller.py

Responsabilidad:
Controlar la lógica de usuarios entre
Vista y Modelo.

Arquitectura:
MVC - Capa Controlador
=========================================================
"""


from models.usuario_model import UsuarioModel



class UsuarioController:


    def __init__(self):

        self.modelo = UsuarioModel()



    # =====================================================
    # LOGIN
    # =====================================================

    def login(self, nombre, password):


        usuario = self.modelo.validar_usuario(
            nombre,
            password
        )


        return usuario



    # =====================================================
    # REGISTRAR USUARIO
    # =====================================================

    def registrar_usuario(
            self,
            nombre,
            password,
            rol
        ):


        return self.modelo.registrar_usuario(
            nombre,
            password,
            rol
        )



    # =====================================================
    # LISTAR USUARIOS
    # =====================================================

    def obtener_usuarios(self):


        return self.modelo.obtener_usuarios()



    # =====================================================
    # ELIMINAR USUARIO
    # =====================================================

    def eliminar_usuario(self, id_usuario):


        return self.modelo.eliminar_usuario(
            id_usuario
        )



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


        return self.modelo.actualizar_usuario(
            id_usuario,
            nombre,
            password,
            rol
        )