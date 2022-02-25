from ast import Break
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
    repeticion = 0
    while True:    
        d1 = np.random.randint(1,7)
        d2 = np.random.randint(1,7)

        num = d1+d2
        repeticion = repeticion +1
        print(num)

        if (num ==8):
            res="ganaste"
            print(res)
            break
        elif(num ==7):
            res="perdiste"
            print(res)
            break
        else:
            res="repite"
            print(res)


    print("Dado 1: ",d1,"Dado 2: ",d2, res, "en el numero de repeticón: ",repeticion)


    try:
        cursor.execute("INSERT INTO JUEGO VALUES (%s,%s,%s,%s);", (d1,d2, res, repeticion))
        conexion.commit()
        print("dato insertado")
    except ValueError:
        print("no se inserto dato")
       

def historial():
    SQL = "SELECT * FROM JUEGO;"
    cursor.execute(SQL)
    valores = cursor.fetchall()
    for row in valores:
        print("DADO 1  = ", row[0])
        print("DADO 2  = ", row[1])
        print("RESULTADO  = ", row[2])
        print("REPETICION = ", row[3], "\n")    

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
