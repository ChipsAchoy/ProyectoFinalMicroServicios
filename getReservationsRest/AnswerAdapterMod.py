from ReservationDatabaseControllerMod import ReservationDatabaseController
from AnswerGeneratorMod import AnswerGenerator
import json

class AnswerAdapter:


    def __init__(self):

        self.resDatabaseController = ReservationDatabaseController()
        self.answerGenerator = AnswerGenerator()


    def retrieve_get_user(self, id_user):
        
        reservationJson = self.answerGenerator.generate_success_response(200, self.resDatabaseController.getByIdUser(id_user))
        return reservationJson
