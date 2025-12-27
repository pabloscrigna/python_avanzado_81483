from flask import Flask, request, jsonify

# simularar una DB
alumnos = []
campos = ("name", "courses")

# app flask
app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False

# endpoint o rutas o recursos
# http://localhost:7001/
@app.route("/")
def test():
    return jsonify({"mensaje": "Recurso no valido"}), 404

# limit skip offset sort
@app.route("/student", methods=["GET"])
def mostrar_alumnos():
    return jsonify({"students": alumnos}), 200

# buscar por indice en la lista
@app.route("/student/<int:dato_id>", methods=["GET"])
def get_uno(dato_id):
    try:
        return jsonify(alumnos[dato_id]), 200
    except IndexError:
        return jsonify({"Mensaje": "Error, no se encuentra ese dato"}), 404


@app.route("/student", methods=["POST"])
def post_alumno():
    # POST desde el cliente , tomo con request
    try:
        auth_header = request.headers.get("Authorization")
        print("authorization: ", auth_header)
        body = request.get_json()  # obtener el contenido de lo que envio el cliente
    except Exception:
        return jsonify({"Mensaje": "Bad Request"}), 400
    for key in body:
        if key not in campos:
            return jsonify({"Mensaje": "Bad Request"}), 400
    nuevo = {"id": len(alumnos), "nombre": body["name"], "cursos": body["courses"]}
    alumnos.append(nuevo)
    return jsonify({"id": nuevo["id"]}), 201


@app.route("/student/<int:dato_id>", methods=["PUT"])
def put_alumno(dato_id):
    # PUT desde el cliente, tomo con request
    try:
        body = (
            request.get_json()
        )  # obtener el contenido de lo que envio el cliente para modificar
        print(body)
    except Exception:
        return jsonify({"Mensaje": "Bad Request"}), 400
    try:
        if "name" in body and "courses" in body:
            alumnos[dato_id]["nombre"] = body["name"]
            alumnos[dato_id]["cursos"] = body["courses"]
            return jsonify({"Mensaje": "Modificado"}), 204
        elif "name" in body:
            alumnos[dato_id]["nombre"] = body["name"]
            return jsonify({"Mensaje": "Modificado"}), 204
        elif "courses" in body:
            alumnos[dato_id]["cursos"] = body["courses"]
            return jsonify({"Mensaje": "Modificado"}), 204
        else:
            return jsonify({"Mensaje": "No existe el campo"}), 204
    except IndexError:
        return jsonify({"Mensaje": "No existe ese id"}), 404

# elimina un id
@app.route("/student/<int:dato_id>", methods=["DELETE"])
def delete_alumno(dato_id):
    try:
        # borro alumno id
        del alumnos[dato_id]
        # actualizar los id´s
        for n in range(0, len(alumnos)):
            alumnos[n]["id"] = n
        return jsonify({"Mensaje": "Borrado"}), 204
    except IndexError:
        return jsonify({"Mensaje": "Error, no se encontro"}), 202


# default port 80
# localhost:7001/
app.run("localhost", port="7001")
