from modelos import Rol, Grupos
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField, TelField, SelectField, BooleanField, TextAreaField
from wtforms.validators import InputRequired, Length, Optional, Email, DataRequired

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
    
    rol_id = SelectField('Rol', coerce=int, validators=[InputRequired()])

    def __init__(self, include_admin=False):
        super(RegistrationForm, self).__init__()
        roles = [(rol.id, rol.rol) for rol in Rol.query.all()]
        
        if not include_admin:
            roles = [(id, rol) for id, rol in roles if rol.lower() != 'admin']

        roles = sorted(roles, key=lambda x: x[0])
        self.rol_id.choices = roles


    contrasena = PasswordField(validators=[InputRequired(), Length(
        min=8, message='La contraseña debe tener al menos 8 caracteres')],
        render_kw={'placeholder':'Contraseña'})
    
    consent = BooleanField('Consiento el uso de mis datos personales por parte de la institución educativa', validators=[DataRequired()])
    
    submit = SubmitField('Registrarse')

    update = SubmitField('Actualizar')

class LoginForm(FlaskForm):
    email = EmailField(validators=[InputRequired(), Email(
        message='Debe ingresar un correo válido')], 
        render_kw={'placeholder':'Correo electrónico'})

    contrasena = PasswordField(validators=[InputRequired(), Length(
        min=8, message='La contraseña debe tener al menos 8 caracteres')],
        render_kw={'placeholder':'Contraseña'})
    
    mantener_sesion = BooleanField('Mantener sesión iniciada')

    submit = SubmitField('Iniciar Sesión')

class AnuncioForm(FlaskForm):
    titulo = StringField(validators=[DataRequired(), Length(min=4, max=30)], render_kw={'placeholder':'Título'})
    texto = TextAreaField(validators=[DataRequired()], render_kw={'placeholder':'Redacte su anuncio'})

    grupos = Grupos.query.order_by(Grupos.id).all()

    choices = [(str(grupo.id), grupo.grupo) for grupo in grupos]
    
    
    # Crea el campo SelectField con las opciones
    default_group_id = next((str(grupo.id) for grupo in grupos if grupo.id == 1), None)
    
    # Crea el campo SelectField con las opciones y el valor predeterminado
    destinatario = SelectField('Visible para:', choices=choices, coerce=int, default=default_group_id)

    submit = SubmitField('Publicar Anuncio')

    update = SubmitField('Actualizar Anuncio')

class RifaForm(FlaskForm):
    nombre = StringField(validators=[InputRequired(), Length(
        min=3, max=90, message='Debe tener un mínimo de 3 caracteres')]
        , render_kw={'placeholder':'Nombre'})

    tel = TelField(validators=[InputRequired(), Length(10, 
        message='Debe ingresar un número de teléfono válido')],
        render_kw={'placeholder':'Teléfono'})
    
    submit = SubmitField('Inscribirme al sorteo')

