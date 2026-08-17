"""
=========================================================
Archivo:
controllers/libro_controller.py

Responsabilidad:
Controlar la logica de gestion de libros.
Arquitectura: MVC - Capa Controlador
=========================================================
"""


from services.libro_service import LibroService


class LibroController:


    def __init__(self):

        self.servicio = LibroService()


    def guardar(self, isbn, titulo, autor, editorial, anio, categoria, cantidad, disponible):

        self.servicio.registrar_libro(isbn, titulo, autor, editorial, anio, categoria, cantidad, disponible)


    def listar(self):

        return self.servicio.listar_libros()


    def buscar(self, texto):

        return self.servicio.buscar_libro(texto)


    def obtener(self, id_libro):

        return self.servicio.obtener_libro(id_libro)


    def actualizar(self, id_libro, isbn, titulo, autor, editorial, anio, categoria, cantidad, disponible):

        self.servicio.actualizar_libro(id_libro, isbn, titulo, autor, editorial, anio, categoria, cantidad, disponible)


    def eliminar(self, id_libro):

        self.servicio.eliminar_libro(id_libro)
