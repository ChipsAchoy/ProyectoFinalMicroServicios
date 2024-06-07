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


    def add_reservation(self, date, time, state, people_quant, id_user, id_rest):

        response = self.answer_adapter.retrieve_add_res(date, time, state, people_quant, id_user, id_rest)
        return response





#controller = UserRequestController()


#if __name__ == "__main__":
#    app.run(host='0.0.0.0', port=8777)
