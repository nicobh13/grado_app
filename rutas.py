
from flask import render_template
from config import app
from modelos import teachers

@app.route('/')
def home():
    return render_template('index.html', teachers=teachers)

#Inicio de esión y Registro
    
#Talleres
@app.route('/especialidades')
def talleres():
    return render_template('talleres.html')
