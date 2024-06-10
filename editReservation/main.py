from UserRequestController import UserRequestController
from flask import Flask, request, jsonify
from Encryption import *

app = Flask(__name__)


@app.route('/edit_reservation', methods=['POST'])
def edit_reservation():
#def edit_reservation():


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
    data = decrypt_responseAPI(data,get_secret_key())
    
    id_r = data['id']
    state = data['state']
    people_quant = data['people_quant']
    id_user = data['id_user']
    id_rest = data['id_rest']
    
    headers = {"Access-Control-Allow-Origin": "*"}

    if not state:
        response = controller.answer_generator.generate_error_response(462, "State is empty")
        return (response, 462, headers)
    if not id_r:
        response = controller.answer_generator.generate_error_response(463, "ID is empty")
        return (response, 463, headers)

    if people_quant == None:
        response = controller.answer_generator.generate_error_response(463, "people_quant is empty")
        return (response, 463, headers)

    
    response = controller.edit_reservation(id_r, state, people_quant, id_user, id_rest)
    response = encrypt_fullmessage(response)
    
    return (response, 200, headers)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8777)
