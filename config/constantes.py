"""
=========================================================
Archivo: constantes.py

Ubicación:
Proyecto_bibiblioteca/config/

Responsabilidad:
Configuración general del sistema.
=========================================================
"""

import os

# Carpeta raíz del proyecto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Carpeta donde se guarda la base de datos
DATABASE_FOLDER = os.path.join(BASE_DIR, "database")

# Nombre de la base de datos
DATABASE_NAME = "biblioteca.db"

# Ruta completa
DATABASE_PATH = os.path.join(DATABASE_FOLDER, DATABASE_NAME)

# Tiempo de espera de SQLite (segundos)
DATABASE_TIMEOUT = 30

# Información del sistema
NOMBRE_SISTEMA = "Sistema de Gestión Bibliotecaria"
VERSION = "1.0.0"