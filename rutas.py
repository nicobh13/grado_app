
from flask import render_template
from config import app
from modelos import teachers

@app.route('/')
def home():
    return render_template('index.html', teachers=teachers)

#Inicio de esión y Registro
    
#Talleres
@app.route('/talleres/<taller>')
def talleres(taller):
    return render_template(f'{taller}.html')

@app.route('/acerca_de')
def acerca_de():
    return render_template('about.html')