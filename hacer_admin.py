from config import db
from modelos import Usuario  # Asegúrate de importar el modelo de Usuario adecuadamente

# Email del usuario que se convertirá en administrador
target_email = 'usuario@promover'

# Recupera el usuario basado en su dirección de correo electrónico
user_to_promote = Usuario.query.filter_by(email=target_email).first()

if user_to_promote:
    # Asigna el rol de administrador (por ejemplo, 1) al usuario
    user_to_promote.rol_id = 1  # Puedes usar un valor que represente "administrador" en tu base de datos

    # Guarda los cambios en la base de datos
    db.session.commit()
    print(f'El usuario {user_to_promote.email} ha sido promovido a administrador.')
else:
    print(f'No se encontró un usuario con el correo {target_email}.')
