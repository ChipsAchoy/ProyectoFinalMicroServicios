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
    

    
    def get_state(self, is_free):
        return "Free" if not is_free else "Booked"

    def set_state(self, state):
        if (state == "Free"):
            return False
        else:
            return True
    

    def edit_reservation(self, reservation_id, state, people_quant, id_user, id_rest):
       
        with self.conn:
            with self.conn.cursor() as cursor:
        

                # Consulta SQL para actualizar una reserva existente
                sql_query = """
                    UPDATE Reservaciones
                    SET estado = %s,
                        people_quant = %s,
                        id_usuario = %s,
                        id_rest = %s
                    WHERE id = %s
                """

                try:
                    # Ejecutar la consulta SQL con los parámetros proporcionados
                    cursor.execute(sql_query, (self.set_state(state), people_quant, id_user, id_rest, reservation_id))
                    self.conn.commit()  # Confirmar la transacción
                    print(f"Reserva con ID {reservation_id} actualizada exitosamente.")
                except Exception as e:
                    self.conn.rollback()  # Revertir la transacción si hay un error
                    print(f"Error al actualizar la reserva: {e}")

        
        



                
