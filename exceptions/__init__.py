class UsuarioError(Exception):
    """Excepción base — permite atrapar cualquier error de Usuario con un solo except."""
    pass

class CedulaInvalidaError(UsuarioError):
    pass

class CorreoInvalidoError(UsuarioError):
    pass

class UsuarioDuplicadoError(UsuarioError):
    pass

class UsuarioNoEncontradoError(UsuarioError):
    pass