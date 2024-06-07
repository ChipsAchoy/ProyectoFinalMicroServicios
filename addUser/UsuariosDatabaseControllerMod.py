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

    def insert_user(self, pw, email, name, lname, direct, access, id_rest):
        try:
            with self.conn:
                with self.conn.cursor() as cursor:
                    sql_query = """
                        INSERT INTO Usuario (contrasena, correo, nombre, apellido, direccion, nivel_acceso, id_rest) VALUES
                        (%s, %s, %s, %s, %s, %s, %s)
                    """
                    encrypted_pw = self.encrypt_password(pw)
                    cursor.execute(sql_query, (encrypted_pw, email, name, lname, direct, access, id_rest))
                    self.conn.commit()
                    print("Usuario insertado exitosamente.")
        except Exception as e:
            print(f"Error: {e}")
            return {}
                
