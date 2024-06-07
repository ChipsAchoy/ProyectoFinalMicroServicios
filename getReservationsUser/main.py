from UserRequestController import UserRequestController
from flask import Flask, request, jsonify


app = Flask(__name__)



@app.route('/get_reservation_user', methods=['GET'])
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

    data = request.args

    id_user = data['id']

    headers = {"Access-Control-Allow-Origin": "*"}

    if not id_user:
        response = controller.answer_generator.generate_error_response(464, "Usuario del ID is empty")
        return (response, 200, headers)

    response = controller.get_user_reservation(id_user)
    
    return (response, 200, headers)



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8777)
