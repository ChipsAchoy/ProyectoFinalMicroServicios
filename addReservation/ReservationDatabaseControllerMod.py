import json
import pymysql
import os
import datetime
class ReservationDatabaseController:

    def __init__(self):

        self.conn = pymysql.connect(
        host='34.171.46.56',  # Reemplaza con la IP de tu instancia
        user='user',
        password='123',
        database='MyRestaurantDataBase',
        cursorclass=pymysql.cursors.DictCursor
        )

        
    def get_state(self, is_free):
        return "Free" if not is_free else "Booked"

    def set_state(self, state):
        if (state == "Free"):
            return False
        else:
            return True
    

    def insert_reservation(self, date, time, state, people_quant, id_user, id_rest):
        try:
            with self.conn.cursor() as cursor:
                # Consulta SQL para insertar una nueva reserva
                sql_query = """
                    INSERT INTO Reservaciones (hora, fecha, estado, people_quant, id_usuario, id_rest)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """

                # Convertir cadena de fecha a formato MySQL DATE ('YYYY-MM-DD')
                fecha_mysql = datetime.datetime.strptime(date, "%Y-%m-%d").date().strftime("%Y-%m-%d")

                # Convertir cadena de hora a formato MySQL TIME ('HH:MM:SS')
                hora_mysql = datetime.datetime.strptime(time, "%H:%M").time().strftime("%H:%M:%S")

                # Ejecutar la consulta SQL con los parámetros proporcionados
                cursor.execute(sql_query, (hora_mysql, fecha_mysql, self.set_state(state), people_quant, id_user, id_rest))
                self.conn.commit()  # Confirmar la transacción

                return 1
                print("Reserva insertada exitosamente.")
        except pymysql.MySQLError as e:
            
                print(e)
                self.conn.rollback()
                return 0
                
