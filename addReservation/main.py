from UserRequestController import UserRequestController
from flask import Flask, request, jsonify
from Encryption import *


app = Flask(__name__)



@app.route('/add_reservation', methods=['POST', 'OPTIONS'])
def add_reservation():
    if request.method == "OPTIONS":
        headers = {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods":  "GET, POST, PUT, DELETE, OPTIONS",
            "Access-Control-Allow-Headers": "Content-Type",
            "Access-Control-Max-Age": "3600",
        }
        return ("", 204, headers)

    controller = UserRequestController()

    data = request.get_json(silent=True)

    date = data['date']
    time = data['time']
    state = data['state']
    people_quant = data['people_quant']
    id_user = data['id_user']
    id_rest = data['id_rest']
    
    headers = {"Access-Control-Allow-Origin": "*"}

    if not date:
        response = controller.answer_generator.generate_error_response(460, "Date is empty")
        return (response, 460, headers)
    elif not time:
        response = controller.answer_generator.generate_error_response(461, "Time is empty")
        return (response, 461, headers)
    elif not state:
        response = controller.answer_generator.generate_error_response(462, "State is empty")
        return (response, 462, headers)

    response = controller.add_reservation(date, time, state, people_quant, id_user, id_rest)

    response = encrypt_fullmessage(response)
    
    return (response, 200, headers)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8777)
