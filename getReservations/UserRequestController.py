#from flask import Flask, request, jsonify
from AnswerAdapterMod import AnswerAdapter
from AnswerGeneratorMod import AnswerGenerator

#from ReservationDatabaseControllerMod import ReservationDatabaseController
#app = Flask(__name__)

class UserRequestController:
    """
    Controller to handle user requests.
    """

    def __init__(self):
        """
        Initializes the UserRequestController.
        """
        self.answer_adapter = AnswerAdapter()
        self.answer_generator = AnswerGenerator()


    def get_user_reservation(self, id_user):

        response = self.answer_adapter.retrieve_get_user(id_user)
        return response






#controller = UserRequestController()


#if __name__ == "__main__":
#    app.run(host='0.0.0.0', port=8777)
