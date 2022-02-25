from random import random
import psycopg2
import numpy as np
from sympy import ratsimpmodprime

try:
    conexion = psycopg2.connect(
        host="localhost",
        port="5432",
        user="postgres",
        password="contrase",
        dbname="postgres"
    )
    print("conexion exitosa")
except:
    print("No fue posible la conexión")
    
cursor = conexion.cursor()

def insertar():    
    r = np.random.randint(1,1000)
    print(r)
    centenas = int(r/100)
    tmp = r % 100
    decenas = int(tmp/10)
    unidades = tmp % 10
    
    
    
    try:
        cursor.execute("INSERT INTO NUMERO VALUES (%s,%s,%s,%s);", (r,centenas, decenas, unidades))
        conexion.commit()
        print("dato insertado")
    except ValueError:
        print("no se inserto dato")
    
    
    
    print("centenas: ",centenas,"\ndecenas:  ", decenas,"\nunidades: ", unidades)


def historial():
    SQL = "SELECT * FROM NUMERO;"
    cursor.execute(SQL)
    valores = cursor.fetchall()
    for row in valores:
        print("NUMERO  = ", row[0])
        print("CENTENAS  = ", row[1])
        print("DECENAS  = ", row[2])
        print("UNIDADES = ", row[3], "\n")    

while True:
    try:
        print("\nSelecciona una opcion:\
                1) Iniciar programa\
                2) Ver historial\
                3) Cerrar\
                    \n")
        option = int(input())
        if (option == 1):
            insertar()
        elif(option == 2):
            historial()
        elif(option == 3):
            break
    except ValueError:
        print("Solo numeros del menu")