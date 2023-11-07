
from flask import render_template
from config import app
from modelos import teachers

@app.route('/')
def home():
    return render_template('index.html', teachers=teachers)

#Inicio de esión y Registro
    
#Talleres
@app.route('/especialidades/informatica')
def informatica():
    return render_template('informatica.html')

@app.route('/especialidades/electricidad')
def electricidad():
    return render_template('electricidad.html')

@app.route('/especialidades/mecanica')
def mecanica():
    return render_template('mecanica.html')

@app.route('/especialidades/dibujo_industrial')
def dibujo():
    return render_template('dibujo.html')
