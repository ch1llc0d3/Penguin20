from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#instanciamos la base de datos 
db = SQLAlchemy()

#Creamos nuestro modelo de base de datos 
class Participante(db.Model):
    id_participante = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(20), nullable=False)
    apellido = db.Column(db.String(20))
    edad = db.Column(db.Integer)
    estado_civil = db.Column(db.String(10))
