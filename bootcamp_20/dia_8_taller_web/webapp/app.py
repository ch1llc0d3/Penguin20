from flask import Flask, render_template #Importar la clase 'Flask' del framework flask para poder construir mi app
import requests

app = Flask(__name__) #Inicialice mi app Flask

@app.route('/') #ruta para que nuestra app pueda ser accedida desed el navegador
def index(): #funcion llamada indez que va a ejecutar cuando ingresemos a la ruta principal
    dibujo = 'Hola Mundo'

    return dibujo

@app.route('/ejemplo') #ruta para que nuestra app pueda ser accedida desed el navegador
def ejemplo(): #funcion llamada indez que va a ejecutar cuando ingresemos a la ruta principal

    return render_template('ejemplo.html')


@app.route('/personaje')
def personaje(): 
    #Definimos la URL a la que se hace el pedido
    api_url = "https://rickandmortyapi.com/api/character/408"

    respuesta_api = requests.get(api_url).json()
    
    nombre = respuesta_api['name']
    estado = respuesta_api['status']
    url_imagen = respuesta_api['image']

    return render_template('personaje.html',
    nombre=nombre, estado=estado, url_imagen=url_imagen)

@app.route('/lista_personajes')
def lista_personajes():
    
    url = "https://rickandmortyapi.com/api/character"

    respuesta_api = requests.get(url).json()

    lista_de_personajes = respuesta_api['results']

    return render_template('lista_personajes.html', 
    lista_de_personajes=lista_de_personajes)



#COnfiguramos para correr con e lboton de play
if __name__ == '__main__':
    app.run(debug = True)