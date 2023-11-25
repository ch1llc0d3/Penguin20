from flask import Flask, render_template, request, redirect, url_for
from modelos import db, Participante

#intrucciones un objeto a partir de la clase Flask
app = Flask(__name__)

#configuraciones de base de datos
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///database.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#inicializamos la base de datos
db.init_app(app)

#RUTAS
@app.route('/')
def index():
    #alumno = 'jorge'
    #edad = 20
    #ESTIRAR DATOS DE LA BASE DE DATOS
    participantes = Participante.query.all()

    return render_template('index.html',participantes_html = participantes)



@app.route('/crear',methods = ['POST'])
def crear():
    if request.method == 'POST':
        #OBTENER DATOS DESDE EL FROM (DESDE UN FORMULARIO)
        nombre = request.form.get('nombre')
        apellido = request.form.get('apellido')
        edad = request.form.get('edad')
        estado_civil = request.form.get('estado_civil')
        #creamos el objeto tipo participante
        participante = Participante(nombre=nombre, apellido=apellido, edad=edad, estado_civil=estado_civil)


    #anhadimos a la base de datos
    db.session.add(participante)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/eliminar/<id>')
def eliminar(id):
    #obtener un solo participante a eliminar segun id
    participante = Participante.query.get(id)
    #eliminar de la base de datos
    db.session.delete(participante)
    db.session.commit()
    #mostrar en index
    return redirect(url_for('index'))

@app.route('/editar/<id>',methods=['GET','POST'])
def editar(id):
    participante = Participante.query.get(id)
    if request.method == 'POST':

        nombre = request.form.get('nombre')
        apellido = request.form.get('apellido')
        edad = request.form.get('edad')
        estado_civil = request.form.get('estado_civil')
        #cargar la info al objeto
        participante.nombre=nombre
        participante.apellido=apellido
        participante.edad=edad
        participante.estado_civil=estado_civil
        
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('editar.html',participante = participante)











if __name__ == '__main__':
    app.run(debug = True)