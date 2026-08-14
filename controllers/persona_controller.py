"""
=========================================================
Archivo:
controllers/persona_controller.py

Responsabilidad:
Controlar la lógica de gestión de usuarios biblioteca.

Arquitectura:
MVC - Capa Controlador
=========================================================
"""


from models.persona_model import PersonaModel



class PersonaController:


    def __init__(self):

        self.modelo = PersonaModel()



    # =====================================================
    # GUARDAR
    # =====================================================

    def guardar(self, datos):

        self.modelo.guardar_persona(datos)



    # =====================================================
    # LISTAR
    # =====================================================

    def listar(self):

        return self.modelo.obtener_personas()



    # =====================================================
    # BUSCAR
    # =====================================================

    def buscar(self, texto):

        return self.modelo.buscar_persona(texto)



    # =====================================================
    # ACTUALIZAR
    # =====================================================

    def actualizar(self, datos):

        self.modelo.actualizar_persona(datos)



    # =====================================================
    # ELIMINAR
    # =====================================================

    def eliminar(self, id_persona):

        self.modelo.eliminar_persona(id_persona)