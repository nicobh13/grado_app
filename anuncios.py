from flask import flash, redirect, render_template, url_for, request
from config import app, db
from log import login_required, logout_user, login_manager, current_user
from modelos import Posts
from forms import AnuncioForm


@app.route('/crear_anuncio', methods=['GET', 'POST'])
@login_required
def crear_anuncio():
    if current_user.rol.rol in ["Admin", "Docente", "Directivo"]:
        form = AnuncioForm()

        if request.method == 'POST' and form.validate_on_submit():
            # Procesa el formulario
            titulo = form.titulo.data.title()
            texto = form.texto.data.title()
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
            flash('Se agregó el anuncio', 'success')


            return redirect(url_for('dashboard'))
        
        return render_template ('nuevo_anuncio.html', form=form)

    else:
        flash('No tienes autorización para crear un anuncio', 'warning')
        return redirect (url_for('dashboard'))