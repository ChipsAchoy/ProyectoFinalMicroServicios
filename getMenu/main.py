from UserRequestController import UserRequestController
from flask import Flask, request, jsonify


app = Flask(__name__)



@app.route("/GetMenu", methods=["GET"])
#@functions_framework.http
def get_menu():
    controller = UserRequestController()
    response = controller.process_menu()
    headers={
        'Content-Type':'text/json',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type, Authorization',
    }
    return (response,200,headers)




if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8777)
