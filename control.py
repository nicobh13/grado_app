from flask import render_template, flash, redirect, url_for, request
from config import app, db
from modelos import usuarios, Usuario, Grupos
from log import current_user, login_required, logout_user
from forms import RegistrationForm

@app.route('/panel')
@login_required
def panel():
    if current_user.rol.rol == 'Admin':
        return render_template('panel.html', usuarios = usuarios)
    
    else:
        flash('No tienes autorización para acceder a esta página', 'warning')
        return redirect (url_for('dashboard'))

#Ver o actualizar info de usuario
@app.route('/user_info/<int:id>', methods=['GET', 'POST'])
@login_required
def user_info(id):
    form = RegistrationForm(include_admin=current_user.rol.rol == 'Admin')
    nombre_actualizar = Usuario.query.get_or_404(id)
    if current_user.id == id or current_user.rol.rol == 'Admin':

        if request.method == "POST":
            nombre_actualizar.nombre = request.form['nombre']
            nombre_actualizar.seg_nombre = request.form['seg_nombre']
            nombre_actualizar.apellido = request.form['apellido']
            nombre_actualizar.seg_apellido = request.form['seg_apellido']
            nombre_actualizar.email = request.form['email']
            nombre_actualizar.tel = request.form['tel']
            nombre_actualizar.rol_id = request.form['rol_id']

            if nombre_actualizar.rol.rol in ['Docente', 'Directivo']:

                if nombre_actualizar.rol.rol == 'Docente':
                    grupo = Grupos.query.filter_by(grupo='NombreDelGrupoDocente').first()
                else:
                    grupo = Grupos.query.filter_by(grupo='NombreDelGrupoDirectivo').first()

                if grupo:
                    nombre_actualizar.grupo_id = grupo.id
            

            try: 
                db.session.commit()
                flash('Se actualizó la información exitosamente', 'success')
                if current_user.rol.rol == 'Admin':
                    return redirect (url_for('panel'))
                else:
                    return redirect (url_for('dashboard'))
            except:
                flash('No se pudo realizar la actualización', 'error')
                return render_template ('usuario_info.html', form=form, nombre_actualizar = nombre_actualizar, id=id)
        
        else:
            return render_template ('usuario_info.html', form=form, nombre_actualizar = nombre_actualizar, id=id)
        
    else:
        flash('No tienes autorización para acceder a esta página', 'warning')
        return redirect (url_for('dashboard'))
    
@app.route('/eliminar/<int:id>', methods=['GET', 'POST'])
@login_required
def eliminar(id):
    usuario_eliminar = Usuario.query.get_or_404(id)


    try: 
        usuario_eliminar.estado = 'inactivo'
        db.session.commit()
        flash('Se eliminó el usuario', 'warning')
        if usuario_eliminar==current_user:
            logout_user()
        return redirect(url_for('sign', form_type='register'))
    except:
        flash('No se pudo realizar la acción', 'error')
        return redirect(url_for('user_info'))
