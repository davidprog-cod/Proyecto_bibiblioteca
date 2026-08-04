from repositories.usuario_repository import UsuarioRepository
from validators.usuario_validator import validar_cedula, validar_correo, validar_campos_no_vacios
from models.usuario import Usuario
from exceptions.usuario_exceptions import (CedulaInvalidaError, CorreoInvalidoError,
                                            UsuarioDuplicadoError, UsuarioNoEncontradoError)

class UsuarioService:
    """Toda la lógica de negocio vive aquí. Nada de SQL, nada de print()."""

    def __init__(self):
        self.repository = UsuarioRepository()

    def registrar_usuario(self, nombre, apellido, cedula, correo, codigo_uni):
        if not validar_campos_no_vacios(nombre, apellido, cedula, correo, codigo_uni):
            raise ValueError("Todos los campos son obligatorios.")
        if not validar_cedula(cedula):
            raise CedulaInvalidaError(f"La cédula '{cedula}' no es válida.")
        if not validar_correo(correo):
            raise CorreoInvalidoError(f"El correo '{correo}' no tiene formato válido.")
        if self.repository.buscar_por_cedula(cedula):
            raise UsuarioDuplicadoError(f"Ya existe un usuario con la cédula {cedula}.")
        if self.repository.buscar_por_correo(correo):
            raise UsuarioDuplicadoError(f"Ya existe un usuario con el correo {correo}.")

        return self.repository.insertar(Usuario(nombre, apellido, cedula, correo, codigo_uni))

    def listar_usuarios(self):
        return self.repository.listar_todos()

    def buscar_usuario(self, cedula):
        usuario = self.repository.buscar_por_cedula(cedula)
        if not usuario:
            raise UsuarioNoEncontradoError(f"No existe un usuario con la cédula {cedula}.")
        return usuario

    def editar_usuario(self, cedula, nombre=None, apellido=None, correo=None, codigo_uni=None):
        usuario = self.buscar_usuario(cedula)
        if correo and correo != usuario.correo:
            if not validar_correo(correo):
                raise CorreoInvalidoError(f"El correo '{correo}' no tiene formato válido.")
            if self.repository.buscar_por_correo(correo):
                raise UsuarioDuplicadoError(f"Ya existe un usuario con el correo {correo}.")
            usuario.correo = correo
        usuario.nombre = nombre or usuario.nombre
        usuario.apellido = apellido or usuario.apellido
        usuario.codigo_uni = codigo_uni or usuario.codigo_uni
        self.repository.actualizar(usuario)
        return usuario

    def eliminar_usuario(self, cedula):
        usuario = self.buscar_usuario(cedula)
        self.repository.eliminar(usuario.id_usuario)