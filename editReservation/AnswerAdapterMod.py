from ReservationDatabaseControllerMod import ReservationDatabaseController
from AnswerGeneratorMod import AnswerGenerator
import json

class AnswerAdapter:


    def __init__(self):

        self.resDatabaseController = ReservationDatabaseController()
        self.answerGenerator = AnswerGenerator()


    def retrieve_edit_res(self, id_r, state, people_quant, id_user, id_rest):

        self.resDatabaseController.edit_reservation(id_r, state, people_quant, id_user, id_rest)
        reservationJson = self.answerGenerator.generate_success_response(200, "")
        return reservationJson
