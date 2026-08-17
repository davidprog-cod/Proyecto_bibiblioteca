"""
=========================================================
Archivo:
controllers/persona_controller.py

Responsabilidad:
Controlar la logica de gestion de personas/socios.
Arquitectura: MVC - Capa Controlador
=========================================================
"""


from services.persona_service import PersonaService


class PersonaController:


    def __init__(self):

        self.servicio = PersonaService()


    def guardar(self, datos):

        codigo, cedula, nombre, apellido, telefono, correo, direccion = datos

        self.servicio.registrar_persona(codigo, cedula, nombre, apellido, telefono, correo, direccion)


    def listar(self):

        return self.servicio.listar_personas()


    def buscar(self, texto):

        return self.servicio.buscar_persona(texto)


    def actualizar(self, id_persona, datos):

        codigo, cedula, nombre, apellido, telefono, correo, direccion = datos

        self.servicio.actualizar_persona(id_persona, codigo, cedula, nombre, apellido, telefono, correo, direccion)


    def eliminar(self, id_persona):

        self.servicio.eliminar_persona(id_persona)
