from flask import flash, redirect, render_template, url_for, request
from config import app, db
from log import login_required, logout_user, login_manager, current_user
from modelos import Posts, anuncios
from forms import AnuncioForm


@app.route('/crear_anuncio', methods=['GET', 'POST'])
@login_required
def crear_anuncio():
    if current_user.rol.rol in ["Admin", "Docente", "Directivo"]:
        form = AnuncioForm()

        if request.method == 'POST' and form.validate_on_submit():
            # Procesa el formulario
            titulo = form.titulo.data.title()
            texto = form.texto.data
            destino_id = form.destinatario.data
            autor_id = current_user.id  # Esto contendrá el ID del grupo seleccionado

            nuevo_anuncio = Posts(
                titulo = titulo,
                texto = texto,
                destino_id = destino_id,
                autor_id = autor_id
            )                
            db.session.add(nuevo_anuncio)
            db.session.commit()
            flash('Se agregó el anuncio, es posible que los cambios tarden un poco en mostrarse', 'success')


            return redirect(url_for('dashboard'))
        
        return render_template ('nuevo_anuncio.html', form=form)

    else:
        flash('No tienes autorización para crear un anuncio', 'warning')
        return redirect (url_for('dashboard'))
    

@app.route('/editar_anuncio/<int:id>', methods=['GET', 'POST'])
@login_required
def editar_anuncio(id):
        form = AnuncioForm()
        anuncio_actualizar = Posts.query.get_or_404(id)

        if current_user.id == anuncio_actualizar.autor_id:

            if request.method == 'POST' and form.validate_on_submit():
                # Procesa el formulario
                anuncio_actualizar.titulo = request.form['titulo']
                anuncio_actualizar.texto = request.form['texto']
                anuncio_actualizar.destino_id = request.form['destinatario']

                try: 
                    db.session.commit()
                    flash('Se editó el anuncio, es posible que los cambios tarden un poco en mostrarse', 'success')
                    return redirect (url_for('dashboard'))
                except:
                    flash('No se pudo realizar la actualización', 'error')
                    return render_template ('editar_anuncio.html', form=form, anuncio_actualizar=anuncio_actualizar)

        else:
            flash('No puedes editar anuncios que no hayas creado', 'warning')
            return redirect (url_for('dashboard'))
        
        return render_template ('editar_anuncio.html', form=form, anuncio_actualizar=anuncio_actualizar)

