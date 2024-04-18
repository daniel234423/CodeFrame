import cv2 as cv
import imutils as imt
from flask import render_template, Response, redirect, url_for
from app.create_app import aplicacion
from app.connecting import  conexion


app = aplicacion()

foto = cv.VideoCapture(1)  # Cámara de video en la posición 0, que es el dispositivo predeterminado

def obtener_frame():
    while True:
        ret, frame = frames_camara()
        if not ret:
            break
        else:
            yield (b'--frame\r\n'   
                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

def frames_camara():
    ret, frame = foto.read()    
    frame = imt.resize(frame,width=800)
    if not ret:
        return False, None
    _, bufer = cv.imencode(".jpg", frame)
    imagen = bufer.tobytes()
    return True, imagen

@app.route("/camara")
def camara():
    return Response(obtener_frame(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route("/almacenar_foto")
def almacenar_foto():
    ret, frame = foto.read()
    nombre = 1
    if ret:
        nombreImg = str(nombre)+".png"
        cv.imwrite(conexion(nombreImg), frame)
        return redirect(url_for('index'))
    return nombre+1

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)