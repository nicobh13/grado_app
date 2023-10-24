from flask import Flask, render_template, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField, TelField, SelectField, BooleanField
from wtforms.validators import InputRequired, Length, Optional, ValidationError, Email, DataRequired
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate


app=Flask(__name__)
app.secret_key = 'juli2201'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://nmora:nIcollemOra12@127.0.0.1:3306/tecnico'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
migrate = Migrate(app, db)
app.app_context().push()

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_usuario(usuario_id):
    return Usuario.query.get(int(usuario_id))


class Rol(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    rol = db.Column(db.String(50), unique=True, nullable=False)

# Definición de la tabla "usuarios"
class Usuario(db.Model, UserMixin):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(50), nullable=False)
    seg_nombre = db.Column(db.String(20), nullable = True)
    apellido = db.Column(db.String(50), nullable=False)
    seg_apellido = db.Column(db.String(20), nullable = True)
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
    
    rol_id = SelectField('Rol',validators=[InputRequired(
        message='Debe ingresar un rol')],
        choices=[
                ('2', 'Soy estudiante'),
                ('3', 'Soy docente'),
                ('4', 'Soy directivo'),
                ('5', 'Soy padre de Familia')
        ])    
    contrasena = PasswordField(validators=[InputRequired(), Length(
        min=8, message='La contraseña debe tener al menos 8 caracteres')],
        render_kw={'placeholder':'Contraseña'})
    
    consent = BooleanField('Consiento el uso de mis datos personales por parte de la institución educativa', validators=[DataRequired()])
    
    submit = SubmitField('Registrarse')

class LoginForm(FlaskForm):
    email = EmailField(validators=[InputRequired(), Email(
        message='Debe ingresar un correo válido')], 
        render_kw={'placeholder':'Correo electrónico'})

    contrasena = PasswordField(validators=[InputRequired(), Length(
        min=8, message='La contraseña debe tener al menos 8 caracteres')],
        render_kw={'placeholder':'Contraseña'})
    
    mantener_sesion = BooleanField('Mantener sesión iniciada')

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

    if form_registro.validate_on_submit():
        usuario_existe = Usuario.query.filter_by(
        email=form_registro.email.data).first()
        if usuario_existe:
            flash(
                   'El correo ya está registrado'
              )
        else:
            contrasena_hash = bcrypt.generate_password_hash(form_registro.contrasena.data)
            nuevo_usuario = Usuario(nombre=form_registro.nombre.data, seg_nombre=form_registro.seg_nombre.data, 
                    apellido=form_registro.apellido.data, seg_apellido=form_registro.seg_apellido.data, 
                    email=form_registro.email.data, tel=form_registro.tel.data, 
                    rol_id=form_registro.rol_id.data, contrasena=contrasena_hash)
            
            db.session.add(nuevo_usuario)
            db.session.commit()
            return redirect (url_for('sign'))

    if form_login.validate_on_submit():
        usuario=Usuario.query.filter_by(email=form_login.email.data).first()
        if usuario:
            if bcrypt.check_password_hash(usuario.contrasena, form_login.contrasena.data ):
                login_user(usuario)
                return redirect ('dashboard')

    return render_template('sign_up.html', form_registro=form_registro, form_login=form_login)
    
@app.route('/especialidades')
def talleres():
    return render_template('talleres.html')

@app.route('/instalaciones')
def mapa():
    return render_template('mapa.html')
    

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/cerrar_sesion')
@login_required
def cerrar_sesion():
    logout_user()
    return redirect (url_for('sign'))


if __name__ == '__main__':
    app.run(debug=True)