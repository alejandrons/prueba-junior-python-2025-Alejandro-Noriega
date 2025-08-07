import mysql.connector
from mysql.connector import Error
from dotenv import find_dotenv, load_dotenv
import os
from datetime import datetime, timedelta, date

load_dotenv(find_dotenv())

host = os.getenv("MYSQL_HOST")
user = os.getenv("MYSQL_USER")
password = os.getenv("MYSQL_PASSWORD")
database = os.getenv("MYSQL_NAME")

# Creación del objeto de conexión a la base de datos
conn = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)
if not conn.is_connected():
    print("Error al conectar a la base de datos.")
    
else:
    print("Conexión exitosa a la base de datos.")

    # Objeto auxiliar para la ejecución de consultas sobre la base de datos
    cursor = conn.cursor()

    while True:
        print("""\n
        BIENVENIDO A LA BASE DE DATOS DE CLIENTES BAYMA
            
            1. Listar clientes dados de alta activos en los últimos 60 días
            2. Insertar un cliente nuevo en la base de datos
            3. Desactivar un cliente por email
            0. Terminar ejecución
            \n\n
        """)

        m = int(input("> "))
        print("\n")

        if m == 0:
            cursor.close()
            conn.close()
            break
        elif m == 1:
            
            fecha_fin = datetime.today().date()
            fecha_inicio = fecha_fin - timedelta(days=60)

            query = """
                SELECT *
                FROM clientes
                WHERE fecha_alta BETWEEN %s AND %s
                    AND activo = 1
                ORDER BY fecha_alta DESC;
            """

            fechas = (fecha_inicio, fecha_fin)

            try:
                cursor.execute(query,fechas)

                resultados = cursor.fetchall()

                if len(resultados) > 0:
                    print("Clientes activos dados de alta los últimos 60 días")
                    for usuario in resultados:
                        print(usuario)
                else:
                    print("No hay clientes activos dados de alta los últimos 60 días")

            except Error as e:
                print(f"Error durante la ejecución de la consulta: {e}")

        elif m == 2:
            nombre = input("Ingrese el nombre del cliente: ")
            email = input("Ingrese el email del cliente: ")
            fecha = datetime.today().date()

            query = """
                INSERT INTO clientes (nombre, email, fecha_alta)
                VALUES (%s,%s,%s);
            """
            datos = (nombre, email, fecha)

            try:
                cursor.execute(query, datos)
                conn.commit()
                print("Cliente ingresado exitosamente.")

            except Error as e:
                print(f"No se pudo ingresar el nuevo usuario en la base de datos: {e}")

        elif m == 3:
            email = input("Ingrese el email del cliente a desactivar: ")

            nuevo_estado = ("0", email)

            try:
                cursor.execute("""UPDATE clientes SET activo = %s WHERE email = %s""", nuevo_estado)
                conn.commit()

                if cursor.rowcount > 0:
                    print("Cliente desactivado exitosamente.")
                else:
                    print("El cliente no se encuentra en la base de datos.")

            except Error as e:
                print(f"Error durante la ejecución de la consulta: {e}")
        else:
            print("Opción inválida")