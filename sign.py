from flask import redirect, flash, url_for, render_template
from config import app,  db, bcrypt
from modelos import Usuario, Grupos
from log import current_user, login_user
from forms import LoginForm, RegistrationForm


@app.route('/sign', methods=['GET', 'POST'])
def sign():
    if current_user.is_authenticated:
        flash('La sesión ya se encuentra iniciada', 'warning')
        return redirect (url_for('dashboard'))
    
    else:

        form_registro = RegistrationForm()
        form_login = LoginForm()

        if form_registro.validate_on_submit():
            usuario_existe = Usuario.query.filter_by(
            email=form_registro.email.data).first()

            if usuario_existe:
                if usuario_existe.estado == 'inactivo':
                    login_user(usuario_existe)
                    usuario_existe.estado = 'activo'
                    db.session.commit()
                    return redirect (url_for('dashboard'))
                else:
                    flash(
                    'El correo ya está registrado', 'error'
                )
            else:
                contrasena_hash = bcrypt.generate_password_hash(form_registro.contrasena.data)
                # Capitaliza la primera letra de cada palabra en los campos de nombre y apellido
                nombre = form_registro.nombre.data.title()
                seg_nombre = form_registro.seg_nombre.data.title()
                apellido = form_registro.apellido.data.title()
                seg_apellido = form_registro.seg_apellido.data.title()

                nuevo_usuario = Usuario(
                    nombre=nombre,
                    seg_nombre=seg_nombre,
                    apellido=apellido,
                    seg_apellido=seg_apellido,
                    email=form_registro.email.data,
                    tel=form_registro.tel.data,
                    rol_id=form_registro.rol_id.data,
                    contrasena=contrasena_hash
                )

                
                if nuevo_usuario.rol.rol in ['Docente', 'Directivo']:

                    if nuevo_usuario.rol.rol == 'Docente':
                        grupo = Grupos.query.filter_by(grupo='NombreDelGrupoDocente').first()
                    else:
                        grupo = Grupos.query.filter_by(grupo='NombreDelGrupoDirectivo').first()

                    if grupo:
                        nuevo_usuario.grupo_id = grupo.id

                db.session.add(nuevo_usuario)
                db.session.commit()
                flash('Se registró de manera exitosa', 'success')
                login_user(nuevo_usuario)
                return redirect (url_for('dashboard'))

        if form_login.validate_on_submit():
            usuario=Usuario.query.filter_by(email=form_login.email.data).first()
            if usuario :
                if usuario.estado =='inactivo':
                    flash('No se encontró el usuario', 'error')
                else:
                    if bcrypt.check_password_hash(usuario.contrasena, form_login.contrasena.data ):
                        login_user(usuario)
                        return redirect (url_for('dashboard'))
                    else:
                        flash ('La contraseña es incorrecta, intente nuevamente', 'error')
                        return render_template('sign_up.html', form_registro=form_registro, form_login=form_login, form_type='login')
                
            else:
                flash('No se encontró el usuario', 'error')
                return render_template('sign_up.html', form_registro=form_registro, form_login=form_login, form_type='register')
            

    return render_template('sign_up.html', form_registro=form_registro, form_login=form_login)
