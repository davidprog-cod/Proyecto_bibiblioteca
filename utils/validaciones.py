"""
=========================================================
Archivo:
validaciones.py

Ubicación:
utils/

Responsabilidad:
Contener validaciones generales del sistema.
=========================================================
"""


import re





def validar_campo_vacio(valor):
    """
    Verifica si un campo está vacío.

    Retorna:
    True  -> está vacío
    False -> tiene información
    """

    if valor is None:

        return True


    return valor.strip() == ""







def validar_correo(correo):
    """
    Valida formato de correo electrónico.
    """


    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'


    return re.match(
        patron,
        correo
    ) is not None







def validar_cedula(cedula):
    """
    Validación básica de cédula ecuatoriana.

    Reglas:
    - Solo números.
    - 10 dígitos.
    """


    if cedula is None:

        return False



    return (
        cedula.isdigit()
        and len(cedula) == 10
    )