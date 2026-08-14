import re

def validar_cedula(cedula):
    """Valida formato básico de cédula ecuatoriana: 10 dígitos numéricos."""
    return cedula.isdigit() and len(cedula) == 10

def validar_correo(correo):
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(patron, correo) is not None

def validar_campos_no_vacios(*campos):
    return all(campo and campo.strip() != "" for campo in campos)