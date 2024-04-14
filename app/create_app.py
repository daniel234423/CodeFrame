from flask import Flask
from app.config import Config

def aplicacion():
    app =  Flask(__name__)
    app.config.from_object(Config)
    return app
