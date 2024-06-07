from ReservationDatabaseControllerMod import ReservationDatabaseController
from AnswerGeneratorMod import AnswerGenerator
import json

class AnswerAdapter:


    def __init__(self):

        self.resDatabaseController = ReservationDatabaseController()
        self.answerGenerator = AnswerGenerator()


    def retrieve_add_res(self, date, time, state, people_quant, id_user, id_rest):
        response = self.resDatabaseController.insert_reservation(date, time, state, people_quant, id_user, id_rest)
        reservationJson = self.answerGenerator.generate_success_response(200, response)
        return reservationJson

