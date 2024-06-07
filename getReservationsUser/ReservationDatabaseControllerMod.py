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
    

    def getByIdUser(self, id_user):

        with self.conn:
            with self.conn.cursor() as cursor:
            
                sql_query = "SELECT * FROM Reservaciones WHERE id_usuario = %s"
                cursor.execute(sql_query, id_user)
                reservations = cursor.fetchall()

                #print(reservations)
                result = []

                # Procesar cada tupla de datos y convertir en formato JSON
                for item in reservations:
                    id_str = item['id']
                    time_str = item['hora']
                    date_str = item['fecha'].strftime('%Y-%m-%d')
                    is_free = item['estado']
                    people_quant = item['people_quant']
                    id_user = item['id_usuario']
                    id_rest = item['id_rest']
                    time_formatted = str(time_str)  # Obtener solo la hora sin microsegundos
                    state = self.get_state(is_free)
                    
                    if len(time_formatted)==7:
                        time_formatted = '0'+ time_formatted
                    
                    # Construir el objeto JSON para cada elemento
                    json_obj = {
                        "id" : id_str,
                        "date": date_str,
                        "time": time_formatted,
                        "state": state,
                        "people_quant": people_quant,
                        "id_user": id_user,
                        "id_rest": id_rest
                    }
                    result.append(json_obj)
                    # Agregar el objeto JSON al resultado
                #print(result)
                    
                

                return result
        
                
