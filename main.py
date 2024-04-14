from flask import render_template
import cv2 as cv
from app.create_app import aplicacion

app = aplicacion()

cam = cv.VideoCapture(0)  # Cámara de video en la posición 0, que es el dispositivo predeterminado

@app.route("/")
def index():
    return render_template("index.html")

app.run(debug=True)