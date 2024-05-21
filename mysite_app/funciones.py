from django.db import connection

# listados de inmuebles por comunas
def consultar_inmuebles_por_comunas():
    with connection.cursor() as cursor:
        
        sql_query = """
        SELECT c.nombre AS comuna, i.nombre AS inmueble, i.descripcion
        FROM mysite_app_comuna c
        INNER JOIN mysite_app_inmueble i ON c.id = i.comuna_id
        """
        cursor.execute(sql_query)
        inmuebles_por_comuna = cursor.fetchall()

    # guardar en archivo de texto
    with open('inmuebles_por_comuna.txt', 'w') as file:
        for comuna, inmueble, descripcion in inmuebles_por_comuna:
            file.write(f"Comuna: {comuna}\n")
            file.write(f"Inmueble: {inmueble}\n")
            file.write(f"Descripción: {descripcion}\n\n")

#  listados de inmuebles por regiones
def consultar_inmuebles_por_regiones():
    with connection.cursor() as cursor:
        
        sql_query = """
        SELECT r.nombre AS region, i.nombre AS inmueble, i.descripcion
        FROM mysite_app_region r
        INNER JOIN mysite_app_comuna c ON r.id = c.region_id
        INNER JOIN mysite_app_inmueble i ON c.id = i.comuna_id
        """
        cursor.execute(sql_query)
        inmuebles_por_region = cursor.fetchall()

    # guardars en archivo de texto
    with open('inmuebles_por_region.txt', 'w') as file:
        for region, inmueble, descripcion in inmuebles_por_region:
            file.write(f"Región: {region}\n")
            file.write(f"Inmueble: {inmueble}\n")
            file.write(f"Descripción: {descripcion}\n\n")
