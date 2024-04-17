import pymysql

#todo esto dentro de una funcion para despues usar la funcion dentro de las rutas 
connecting = pymysql.connect(host='localhost', user='root', password='Daniel230139', database='codeframe' )
def conexion(nomber):
    cursor = connecting.cursor()
    consulta = "insert into imagenes (img) values (%s)"
    cursor.execute(consulta,(nomber))
    connecting.commit()
    cursor.close()
    connecting.close()



