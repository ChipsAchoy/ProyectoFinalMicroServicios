from UserRequestController import UserRequestController
from flask import Flask, request, jsonify
from Encryption import *

app = Flask(__name__)



@app.route('/get_reservation', methods=['GET' ,'OPTIONS'])
def get_reservation_per_user():


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



    id_user = 0

    headers = {"Access-Control-Allow-Origin": "*"}


    response = controller.get_user_reservation(id_user)
    response = encrypt_fullmessage(response)
    
    return (response, 200, headers)



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8777)
