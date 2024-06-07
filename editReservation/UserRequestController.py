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



    def edit_reservation(self, id_r, state, people_quant, id_user, id_rest):

        response = self.answer_adapter.retrieve_edit_res(id_r, state, people_quant, id_user, id_rest)
        return response




#controller = UserRequestController()


#if __name__ == "__main__":
#    app.run(host='0.0.0.0', port=8777)
