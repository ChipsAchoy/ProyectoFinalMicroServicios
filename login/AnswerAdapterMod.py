from UsuariosDatabaseControllerMod import UsuariosDatabaseController
from AnswerGeneratorMod import AnswerGenerator
import json

class AnswerAdapter:


    def __init__(self):

        self.userDatabaseController = UsuariosDatabaseController()
        self.answerGenerator = AnswerGenerator()

    def retrieve_login(self, pw, email):

        idSend = self.userDatabaseController.login(pw, email)
        userJson = self.answerGenerator.generate_success_response(200, idSend)
        return userJson
