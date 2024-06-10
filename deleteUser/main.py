from UserRequestController import UserRequestController
from flask import Flask, request, jsonify
from Encryption import *

app = Flask(__name__)



@app.route('/deleteUser', methods=['POST'])
def delete_user():


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

    data = request.args
    
    id_u = data['id']


    headers = {"Access-Control-Allow-Origin": "*"}

    if not id_u:
        response = controller.answer_generator.generate_error_response(460, "id_u is empty")
        return (response, 460, headers)
 

    response = controller.delete_user(id_u)
    response = encrypt_fullmessage(response)
    
    return (response, 200, headers)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8777)
