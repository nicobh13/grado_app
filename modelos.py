from config import db, migrate
from flask_login import UserMixin
from datetime import datetime


class Rol(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    rol = db.Column(db.String(50), unique=True, nullable=False)

# Definición de la tabla "usuarios"
class Grupos(db.Model):
    __tablename__ = 'grupos'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    grupo = db.Column(db.String(20), unique = True)

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
    grupo_id = db.Column(db.Integer, db.ForeignKey('grupos.id'), nullable=True)
    contrasena = db.Column(db.String(255), nullable=False)
    fecha_registro = db.Column(db.DateTime, default = datetime.utcnow)
    fecha_actualizado = db.Column(db.DateTime, onupdate=datetime.utcnow)
    estado = db.Column(db.String(20), nullable=False, default='activo')

    # Relación con la tabla "roles"
    grupo = db.relationship('Grupos', foreign_keys = [grupo_id])
    rol = db.relationship('Rol')

    

class Posts(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(30), nullable = False)
    texto = db.Column(db.Text, nullable = False)
    autor_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    fecha_publicado = db.Column(db.DateTime, default = datetime.utcnow)
    fecha_editado = db.Column(db.DateTime, onupdate=datetime.utcnow)
    destino_id = db.Column(db.Integer, db.ForeignKey('grupos.id'), nullable=True)
    visibilidad = db.Column(db.String(30), default = "visible")

    
    # Relación con la tabla "usuarios" para acceder al autor
    autor = db.relationship('Usuario', foreign_keys=[autor_id])
    destino = db.relationship('Grupos', foreign_keys=[destino_id])

usuarios = Usuario.query.order_by(Usuario.apellido)

teachers = [
    {"name": "Teacher 1", "position": "Position 1"},
    {"name": "Teacher 2", "position": "Position 2"},
    {"name": "Teacher 3", "position": "Position 3"},
    {"name": "Teacher 4", "position": "Position 4"}
]
