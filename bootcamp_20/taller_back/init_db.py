from flask import Flask
from modelos import db, Participante

#Instanciamos de la clase flask usando el servidor app
app = Flask('app')

#configuraciones d ela base de datos
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///database.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Inicializamos la base de datos
db.init_app(app)

'''
#Creamos la base de datos 
with app.app_context():
    db.create_all()
'''
#Agregamos datos a la base de datos de forma manual
with app.app_context():

    #Carga de datos
    participante_1 = Participante(nombre='Marcos', apellido='Talavera', edad=23, estado_civil='soltero')
    participante_2 = Participante(nombre='Jose', apellido='Guerrero', edad=34, estado_civil='casado')
    participante_3 = Participante(nombre='Luana', apellido='Rivas', edad=24, estado_civil='soltero')

    db.session.add(participante_1)
    db.session.add(participante_2)
    db.session.add(participante_3)
    db.session.commit()
