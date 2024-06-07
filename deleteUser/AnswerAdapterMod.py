from UsuariosDatabaseControllerMod import UsuariosDatabaseController
from AnswerGeneratorMod import AnswerGenerator
import json

class AnswerAdapter:


    def __init__(self):

        self.userDatabaseController = UsuariosDatabaseController()
        self.answerGenerator = AnswerGenerator()

    def retrieve_delete_user(self,id_u):
        self.userDatabaseController.delete_user(id_u)
        userJson = self.answerGenerator.generate_success_response(200, "")
        return userJson

