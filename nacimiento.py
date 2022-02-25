import psycopg2

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
    while True:
        try:
            x = int(input("Dia de nacimiento: ")) 
            y = int(input("Mes de nacimiento: ")) 
            z = int(input("Año de nacimiento: ")) 
            if (x<32 and y<13 and z<2023):
                break
            else:
                print("valor no valido")
        except ValueError:
            print("Solo numeros")
    if (x < 24 and y < 2):
        cumplido = "Cumplido"
        edad = 2022-z
        c= "ya cumplió años"
    else:
        cumplido = "No cumplido"
        edad = 2022-z-1
        c= "no ha cumplido años aún"

    try:
        cursor.execute("INSERT INTO PERSONAS VALUES (%s,%s,%s,%s,%s);", (x, y, z,edad, cumplido))
        conexion.commit()
        print("dato insertado")
    except ValueError:
        print("no se inserto dato")

    print("Esta persona tiene ",edad, "años y esta persona ",c)
    

def historial():
    SQL = "SELECT * FROM PERSONAS;"
    cursor.execute(SQL)
    valores = cursor.fetchall()
    for row in valores:
        print("DIA  = ", row[0])
        print("MES  = ", row[1])
        print("AÑO  = ", row[2])
        print("EDAD  = ", row[3])
        print("CUMPLIDO = ", row[4], "\n")    

while True:
    try:
        print("\nSelecciona una opcion:\
                1)  Iniciar programa\
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
