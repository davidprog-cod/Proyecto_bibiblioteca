from database.conexion import obtener_conexion
from models.usuario import Usuario

class UsuarioRepository:
    """Único lugar del sistema donde se escribe SQL para la tabla usuarios."""

    def insertar(self, usuario: Usuario):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        query = """
            INSERT INTO usuarios (nombre, apellido, Cedula, Correo, codigo_uni, estado)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (usuario.nombre, usuario.apellido, usuario.cedula,
                                usuario.correo, usuario.codigo_uni, usuario.estado))
        conexion.commit()
        usuario.id_usuario = cursor.lastrowid
        cursor.close()
        conexion.close()
        return usuario

    def buscar_por_cedula(self, cedula):
        return self._buscar_por_campo("Cedula", cedula)

    def buscar_por_correo(self, correo):
        return self._buscar_por_campo("Correo", correo)

    def _buscar_por_campo(self, campo, valor):
        conexion = obtener_conexion()
        cursor = conexion.cursor(dictionary=True)
        cursor.execute(f"SELECT * FROM usuarios WHERE {campo} = %s", (valor,))
        fila = cursor.fetchone()
        cursor.close()
        conexion.close()
        return self._fila_a_usuario(fila) if fila else None

    def listar_todos(self):
        conexion = obtener_conexion()
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuarios")
        filas = cursor.fetchall()
        cursor.close()
        conexion.close()
        return [self._fila_a_usuario(f) for f in filas]

    def actualizar(self, usuario: Usuario):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        query = """
            UPDATE usuarios
            SET nombre=%s, apellido=%s, Correo=%s, codigo_uni=%s, estado=%s
            WHERE id=%s
        """
        cursor.execute(query, (usuario.nombre, usuario.apellido, usuario.correo,
                                usuario.codigo_uni, usuario.estado, usuario.id_usuario))
        conexion.commit()
        cursor.close()
        conexion.close()

    def eliminar(self, id_usuario):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM usuarios WHERE id=%s", (id_usuario,))
        conexion.commit()
        cursor.close()
        conexion.close()

    def _fila_a_usuario(self, fila):
        return Usuario(id_usuario=fila["id"], nombre=fila["nombre"], apellido=fila["apellido"],
                        cedula=fila["Cedula"], correo=fila["Correo"],
                        codigo_uni=fila["codigo_uni"], estado=fila["estado"])   