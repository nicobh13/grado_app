from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField, TelField, SelectField
from wtforms.validators import InputRequired, Length, Optional, ValidationError, Email


app=Flask(__name__)
app.secret_key = 'juli2201'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://nmora:nIcollemOra12@127.0.0.1:3306/tecnico'
db = SQLAlchemy(app)

app.app_context().push()

class Rol(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    rol = db.Column(db.String(50), unique=True, nullable=False)

# Definición de la tabla "usuarios"
class Usuario(db.Model, UserMixin):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(50), nullable=False)
    seg_nombre = db.Column(db.String(20))
    apellido = db.Column(db.String(50), nullable=False)
    seg_apellido = db.Column(db.String(20))
    email = db.Column(db.String(80), unique=True, nullable=False)
    tel = db.Column(db.String(10), nullable=False)
    rol_id = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)
    contrasena = db.Column(db.String(255), nullable=False)

    # Relación con la tabla "roles"
    rol = db.relationship('Rol') 
        
class RegistrationForm(FlaskForm):
    nombre = StringField(validators=[InputRequired(), Length(
        min=3, max=10, message='Debe tener un mínimo de 3 caracteres')]
        , render_kw={'placeholder':'Primer Nombre'})
     
    seg_nombre = StringField(validators=[Optional(), Length(
        min=3, max=10, message='Debe tener un mínimo de 3 caracteres')]
        , render_kw={'placeholder':'Segundo Nombre'})
     
    apellido = StringField(validators=[InputRequired(), Length(
        min=4, max=10, message='Debe tener un mínimo de 4 caracteres')]
        , render_kw={'placeholder':'Primer Apellido'})
     
    seg_apellido = StringField(validators=[Optional(), Length(
        min=4, max=10, message='Debe tener un mínimo de 4 caracteres')]
        , render_kw={'placeholder':'Segundo Apellido'})
    
    email = EmailField(validators=[InputRequired(), Email(
        message='Debe ingresar un correo válido')], 
        render_kw={'placeholder':'Correo electrónico'})
    
    tel = TelField(validators=[InputRequired(), Length(10, 
        message='Debe ingresar un número de teléfono válido')],
        render_kw={'placeholder':'Teléfono'})
    
    contraseña = PasswordField(validators=[InputRequired(), Length(
        min=8, message='La contraseña debe tener al menos 8 caracteres')])
    
    submit = SubmitField('Registrarse')

    def validar_usuario(self, email):
         usuario_existe = Usuario.query.filter_by(
              email=email.data).first()
         if usuario_existe:
              raise ValidationError(
                   'El correo ya está registrado'
              )

class LoginForm(FlaskForm):
    email = EmailField(validators=[InputRequired(), Email(
        message='Debe ingresar un correo válido')], 
        render_kw={'placeholder':'Correo electrónico'})

    contraseña = PasswordField(validators=[InputRequired(), Length(
        min=8, message='La contraseña debe tener al menos 8 caracteres')])

    submit = SubmitField('Iniciar Sesión')

teachers = [
    {"name": "Teacher 1", "position": "Position 1"},
    {"name": "Teacher 2", "position": "Position 2"},
    {"name": "Teacher 3", "position": "Position 3"},
    {"name": "Teacher 4", "position": "Position 4"}
]

@app.route('/')
def home():
    return render_template('index.html', teachers=teachers)

@app.route('/sign', methods=['GET', 'POST'])
def sign():
    form_registro = RegistrationForm()
    form_login = LoginForm()

    return render_template('sign_up.html', form_registro=form_registro, form_login=form_login)
    
@app.route('/especialidades')
def talleres():
    return render_template('talleres.html')

@app.route('/instalaciones')
def mapa():
    return render_template('mapa.html')
    
if __name__ == '__main__':
    app.run(debug=True)


