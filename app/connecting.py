import pymysql

#todo esto dentro de una funcion para despues usar la funcion dentro de las rutas 

connecting = pymysql.connect(host='localhost', user='root', password='Daniel230139', database='codeframe' )

cursor = connecting.cursor()

ruta_img = 'app/static/img/A.png'
with open(ruta_img, 'rb' ) as f:
    imagen_blob =  f.read()
    
text_post = "Hola"
users_idusers = 1
sql = "insert into post (img_post, text_post,users_idusers ) values (%s, %s, %s)"

cursor.execute(sql, (imagen_blob, text_post, users_idusers,))

connecting.commit()
cursor.close()
    
connecting.close()