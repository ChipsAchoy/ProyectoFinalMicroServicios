import json
import pymysql
import os
import datetime
class MenuDatabaseController:

    def __init__(self):

        self.conn = pymysql.connect(
        host='34.171.46.56',  # Reemplaza con la IP de tu instancia
        user='user',
        password='123',
        database='MyRestaurantDataBase',
        cursorclass=pymysql.cursors.DictCursor
        )

        
    def get_menu(self):
        """
        Retrieves the entire menu.

        Returns:
            str: A JSON string representing the entire menu.
        """
        with self.conn:
                with self.conn.cursor() as cursor:
                    sql_query = """
                        SELECT 
                        P.nombre AS Nombre_Platillo,
                        P.descripcion AS Descripcion_Platillo,
                        R.set_rec AS Set_Recomendado,
                        T.tipo AS Tipo_Platillo
                        FROM 
                            Recomendaciones AS R
                        INNER JOIN 
                            Platillos AS P ON R.id_platillo = P.id
                        INNER JOIN 
                            Tipo_Platillos AS T ON P.tipo_id = T.id
                        ORDER BY 
                            R.set_rec;
                    """
                    cursor.execute(sql_query)
                    menu = cursor.fetchall()

                    print(menu)
                    print("len:",len(menu))
                    sets_quant_ref = 3
                    sets_quant = sets_quant_ref
                    
                    menu_set = []
                    menu_set_current = []
                    
                    for platillo in menu:
                        
                        menu_set_current += [platillo]
                        sets_quant -= 1
                        if sets_quant == 0:
                            sets_quant = sets_quant_ref
                            menu_set += [menu_set_current]
                            menu_set_current = []
                        
                    print("menusets:",menu_set)
                    # Lista para almacenar cada set como un objeto JSON
                    result_sets = []
                    
                    for set_platillos in menu_set:
                        # Diccionario para almacenar los platillos de cada tipo
                        set_info = {
                            'dish': None,
                            'drink': None,
                            'dessert': None
                        }

                        # Iterar sobre cada tupla en el set de platillos
                        for platillo in set_platillos:

                            name = platillo['Nombre_Platillo']
                            description = platillo['Descripcion_Platillo']
                            set_rec = platillo['Set_Recomendado']
                            tipo = platillo['Tipo_Platillo']
                            print(name)
                            if tipo == 'dish':
                                set_info['dish'] = {
                                    'name': name,
                                    'description': description
                                }
                            elif tipo == 'drink':
                                set_info['drink'] = {
                                    'name': name,
                                    'description': description
                                }
                            elif tipo == 'dessert':
                                set_info['dessert'] = {
                                    'name': name,
                                    'description': description
                                }
                        
                        # Agregar el set de platillos al resultado
                        result_sets.append(set_info)

                    # Convertir la lista de sets en formato JSON
                    json_data = result_sets
                    print("json:",result_sets)
                    # Imprimir el JSON generado
                    #print(json_data)
                    
                    return json_data
            
        
                
