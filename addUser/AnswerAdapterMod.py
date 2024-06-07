from UsuariosDatabaseControllerMod import UsuariosDatabaseController
from AnswerGeneratorMod import AnswerGenerator
import json

class AnswerAdapter:


    def __init__(self):

        self.userDatabaseController = UsuariosDatabaseController()
        self.answerGenerator = AnswerGenerator()

    def retrieve_add_user(self, pw, email, name, lname, direct, access, id_rest):
        idSend = self.userDatabaseController.insert_user(pw, email, name, lname, direct, access, id_rest)
        userJson = self.answerGenerator.generate_success_response(200, idSend)
        return userJson

