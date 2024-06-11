from UserRequestController import UserRequestController
from flask import Flask, request, jsonify
from Encryption import *

app = Flask(__name__)


#@functions_framework.http
@app.route('/login', methods=['POST'])
def login():


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

    #data = request.json  # Obtener los datos del cuerpo de la solicitud JSON
    
    print("DATA:",request.get_json())
    data = request.get_json()
    data = decrypt_responseAPI(data,get_secret_key())
    print("DATA DECRYPTED:",data)
    
    
    pw = data.get('contrasena')
    email = data.get('correo')
    headers = {"Access-Control-Allow-Origin": "*"}

    if not pw:
        response = controller.answer_generator.generate_error_response(460, "password is empty")
        return (response, 460, headers)

    if not email:
        response = controller.answer_generator.generate_error_response(460, "email is empty")
        return (response, 460, headers)

    response = controller.login(pw, email)  
    print("RESPONSE:",response)
    response = encrypt_fullmessage(response)

    return (response, 200, headers)



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8777)
