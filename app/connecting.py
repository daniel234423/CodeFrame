import pymysql

#todo esto dentro de una funcion para despues usar la funcion dentro de las rutas 

connecting = pymysql.connect(host='localhost', user='root', password='Daniel230139', database='codeframe' )

cursor = connecting.cursor()
'''
ruta_img = 'app/static/img/A.png'
with open(ruta_img, 'rb' ) as f:
    imagen_blob =  f.read()
    
sql = "insert into imagenes (img) values (%s)"

cursor.execute(sql, (imagen_blob,))
'''
mostrar = cursor.execute("select img from imagenes")
print(mostrar)
connecting.commit()
cursor.close()
    
connecting.close()