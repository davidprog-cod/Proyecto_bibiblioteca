"""
=========================================================
Archivo:
backend/api.py

Responsabilidad:
API REST con Flask para conectar el frontend React
con la base de datos SQLite.
=========================================================
"""


import sys

import os


# Agregar la raiz del proyecto al path

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from flask import Flask, request, jsonify

from flask_cors import CORS

from database.crear_bd import CrearBD

from repositories.persona_repository import PersonaRepository

from repositories.libro_repository import LibroRepository

from services.persona_service import PersonaService

from services.libro_service import LibroService


app = Flask(__name__)

CORS(app)


# Crear tablas al iniciar

creador = CrearBD()

creador.crear_tablas()


persona_service = PersonaService()

libro_service = LibroService()


# =====================================================
# PERSONAS
# =====================================================


@app.route("/api/personas", methods=["GET"])

def listar_personas():

    personas = persona_service.listar_personas()

    resultado = []

    for p in personas:

        resultado.append({

            "id": p[0],

            "codigo": p[1],

            "cedula": p[2],

            "nombre": p[3],

            "apellido": p[4],

            "telefono": p[5],

            "correo": p[6],

            "direccion": p[7]

        })

    return jsonify(resultado)


@app.route("/api/personas", methods=["POST"])

def crear_persona():

    data = request.get_json()

    try:

        persona_service.registrar_persona(
            data["codigo"],
            data["cedula"],
            data["nombre"],
            data["apellido"],
            data.get("telefono", ""),
            data.get("correo", ""),
            data.get("direccion", "")
        )

        return jsonify({"mensaje": "Persona creada correctamente"}), 201

    except Exception as e:

        return jsonify({"error": str(e)}), 400


@app.route("/api/personas/<int:id_persona>", methods=["PUT"])

def actualizar_persona(id_persona):

    data = request.get_json()

    try:

        persona_service.actualizar_persona(
            id_persona,
            data["codigo"],
            data["cedula"],
            data["nombre"],
            data["apellido"],
            data.get("telefono", ""),
            data.get("correo", ""),
            data.get("direccion", "")
        )

        return jsonify({"mensaje": "Persona actualizada correctamente"})

    except Exception as e:

        return jsonify({"error": str(e)}), 400


@app.route("/api/personas/<int:id_persona>", methods=["DELETE"])

def eliminar_persona(id_persona):

    try:

        persona_service.eliminar_persona(id_persona)

        return jsonify({"mensaje": "Persona eliminada correctamente"})

    except Exception as e:

        return jsonify({"error": str(e)}), 400


@app.route("/api/personas/buscar")

def buscar_personas():

    q = request.args.get("q", "")

    personas = persona_service.buscar_persona(q)

    resultado = []

    for p in personas:

        resultado.append({

            "id": p[0],

            "codigo": p[1],

            "cedula": p[2],

            "nombre": p[3],

            "apellido": p[4],

            "telefono": p[5],

            "correo": p[6],

            "direccion": p[7]

        })

    return jsonify(resultado)


# =====================================================
# LIBROS
# =====================================================


@app.route("/api/libros", methods=["GET"])

def listar_libros():

    libros = libro_service.listar_libros()

    resultado = []

    for l in libros:

        resultado.append({

            "id": l[0],

            "isbn": l[1],

            "titulo": l[2],

            "autor": l[3],

            "editorial": l[4],

            "anio": l[5],

            "categoria": l[6],

            "cantidad": l[7],

            "disponible": bool(l[8])

        })

    return jsonify(resultado)


@app.route("/api/libros", methods=["POST"])

def crear_libro():

    data = request.get_json()

    try:

        libro_service.registrar_libro(
            data["isbn"],
            data["titulo"],
            data["autor"],
            data.get("editorial", ""),
            data.get("anio", ""),
            data["categoria"],
            data.get("cantidad", 0),
            data.get("disponible", True)
        )

        return jsonify({"mensaje": "Libro creado correctamente"}), 201

    except Exception as e:

        return jsonify({"error": str(e)}), 400


@app.route("/api/libros/<int:id_libro>", methods=["GET"])

def obtener_libro(id_libro):

    try:

        libro = libro_service.obtener_libro(id_libro)

        return jsonify({

            "id": libro[0],

            "isbn": libro[1],

            "titulo": libro[2],

            "autor": libro[3],

            "editorial": libro[4],

            "anio": libro[5],

            "categoria": libro[6],

            "cantidad": libro[7],

            "disponible": bool(libro[8])

        })

    except Exception as e:

        return jsonify({"error": str(e)}), 404


@app.route("/api/libros/<int:id_libro>", methods=["PUT"])

def actualizar_libro(id_libro):

    data = request.get_json()

    try:

        libro_service.actualizar_libro(
            id_libro,
            data["isbn"],
            data["titulo"],
            data["autor"],
            data.get("editorial", ""),
            data.get("anio", ""),
            data["categoria"],
            data.get("cantidad", 0),
            data.get("disponible", True)
        )

        return jsonify({"mensaje": "Libro actualizado correctamente"})

    except Exception as e:

        return jsonify({"error": str(e)}), 400


@app.route("/api/libros/<int:id_libro>", methods=["DELETE"])

def eliminar_libro(id_libro):

    try:

        libro_service.eliminar_libro(id_libro)

        return jsonify({"mensaje": "Libro eliminado correctamente"})

    except Exception as e:

        return jsonify({"error": str(e)}), 400


@app.route("/api/libros/buscar")

def buscar_libros():

    q = request.args.get("q", "")

    libros = libro_service.buscar_libro(q)

    resultado = []

    for l in libros:

        resultado.append({

            "id": l[0],

            "isbn": l[1],

            "titulo": l[2],

            "autor": l[3],

            "editorial": l[4],

            "anio": l[5],

            "categoria": l[6],

            "cantidad": l[7],

            "disponible": bool(l[8])

        })

    return jsonify(resultado)


# =====================================================

if __name__ == "__main__":

    app.run(debug=True, port=5000)
