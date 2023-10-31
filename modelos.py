from config import db
from flask_login import UserMixin
from datetime import datetime


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
    fecha_registro = db.Column(db.DateTime, default = datetime.utcnow)
    fecha_actualizado = db.Column(db.DateTime, onupdate=datetime.utcnow)

    # Relación con la tabla "roles"
    rol = db.relationship('Rol')

usuarios = Usuario.query.order_by(Usuario.apellido)

teachers = [
    {"name": "Teacher 1", "position": "Position 1"},
    {"name": "Teacher 2", "position": "Position 2"},
    {"name": "Teacher 3", "position": "Position 3"},
    {"name": "Teacher 4", "position": "Position 4"}
]
