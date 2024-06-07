import json
import pymysql
import os
import datetime
import bcrypt


class UsuariosDatabaseController:

    def __init__(self):

        self.conn = pymysql.connect(
        host='34.171.46.56',  # Reemplaza con la IP de tu instancia
        user='user',
        password='123',
        database='MyRestaurantDataBase',
        cursorclass=pymysql.cursors.DictCursor
        )
    def encrypt_password(self, password):
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        return hashed_password

    def verify_password(self, input_password, hashed_password):
        return bcrypt.checkpw(input_password.encode('utf-8'), hashed_password.encode('utf-8'))

    def login(self, pw, email):
        try:
            with self.conn:
                with self.conn.cursor() as cursor:
                    sql_query = "SELECT id, contrasena FROM Usuario WHERE correo = %s"
                    cursor.execute(sql_query, email)
                    user_data = cursor.fetchone()

                    if user_data and self.verify_password(pw, user_data['contrasena']):
                        return {'id': user_data['id'], 'correct': True}
                    else:
                        return {'id': 0, 'correct': False}
        except Exception as e:
            print(f"Error: {e}")
            return {}
