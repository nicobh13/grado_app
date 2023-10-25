#Insertar roles en la base de datos

from app import db  # Reemplaza "your_app" con el nombre de tu aplicación
from app import Rol  # Reemplaza "your_app" y "models" con las ubicaciones correctas

def insertar_roles():
    roles = ['Admin', 'Estudiante', 'Docente', 'Directivo', 'Padre']
    
    for rol in roles:
        nuevo_rol = Rol(rol=rol.capitalize())
        db.session.add(nuevo_rol)
    
    db.session.commit()
    print('Roles insertados exitosamente')

if __name__ == '__main__':
    insertar_roles()
