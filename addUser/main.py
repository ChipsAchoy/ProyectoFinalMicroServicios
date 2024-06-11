from UserRequestController import UserRequestController
from flask import Flask, request, jsonify
from Encryption import *

app = Flask(__name__)


#@functions_framework.http
@app.route('/addUser', methods=['POST', 'OPTIONS'])
def add_user():


    if request.method == "OPTIONS":
        # Allows GET requests from any origin with the Content-Type
        # header and caches preflight response for an 3600s
        headers = {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
            "Access-Control-Allow-Headers": "Content-Type",
            "Access-Control-Max-Age": "3600",
        }

        return ("", 204, headers)


    controller = UserRequestController()

    data = request.get_json(silent=True)
    
    pw = data.get('contrasena')
    email = data.get('correo')
    name = data.get('nombre')
    lname = data.get('apellido')
    direct = data.get('direccion')
    access = data.get('nivel_acceso')
    id_rest = data.get('id_rest')


    headers = {"Access-Control-Allow-Origin": "*"}

    if not pw:
        response = controller.answer_generator.generate_error_response(460, "password is empty")
        return (response, 460, headers)
    
    if not email:
        response = controller.answer_generator.generate_error_response(460, "email is empty")
        return (response, 460, headers)

    if not name:
        response = controller.answer_generator.generate_error_response(460, "name is empty")
        return (response, 460, headers)

    if not lname:
        response = controller.answer_generator.generate_error_response(460, "lname is empty")
        return (response, 460, headers)

    if not direct:
        response = controller.answer_generator.generate_error_response(460, "direct is empty")
        return (response, 460, headers)

    if access == None:
        response = controller.answer_generator.generate_error_response(460, "access is empty")
        return (response, 460, headers)

    response = controller.add_user(pw, email, name, lname, direct, access, id_rest)

    response = encrypt_fullmessage(response)
    return (response, 200, headers)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8777)
