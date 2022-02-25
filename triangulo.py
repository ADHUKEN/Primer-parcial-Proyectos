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
            P_a = float(input("Ingrese primer angulo: "))
            S_a = float(input("Ingrese segundo angulo: "))
            if (P_a+S_a >= 179):
                print("angulos invalidos")
            else:
                break
        except ValueError:
            print("invalido")
        
        
        
    T_a = 180 - P_a - S_a


    try:
        cursor.execute("INSERT INTO TRIANGULO VALUES (%s,%s,%s);", (P_a, S_a, T_a))
        conexion.commit()
        print("dato insertado")
    except ValueError:
        print("no se inserto dato")

    print("El tercer angulo del triangulo es ",T_a)


def historial():
    SQL = "SELECT * FROM TRIANGULO;"
    cursor.execute(SQL)
    valores = cursor.fetchall()
    for row in valores:
        print("PRIMER ANGULO  = ", row[0])
        print("SEGUNDO ANGULO  = ", row[1])
        print("TERCER ANGULO = ", row[2], "\n")    

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