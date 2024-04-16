from flask import render_template, Response
import cv2 as cv
import imutils as imt
from app.create_app import aplicacion

app = aplicacion()

cam = cv.VideoCapture(0)  # Cámara de video en la posición 0, que es el dispositivo predeterminado

def obtener_frame():
    while True:
        ret, frame = frames_camara()
        if not ret:break
        else:
            yield b"--frame\r\n content-Type: image/jpeg\r\n"+ frame + b"\r\n"

def frames_camara():
    ret, frame = cam.read()    
    if not ret:
                    return False, None
    _, bufer = cv.imdecode('png', frame)
    imagen = bufer.tobytes()
    return True, imagen

@app.route("/camara")
def camara():
    return Response(obtener_frame())
@app.route("/")
def index():
    return render_template("index.html")

app.run(debug=True)