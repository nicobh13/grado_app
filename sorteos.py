from flask import flash, redirect, render_template, url_for
from config import app, db
from random import choice
from forms import RifaForm
from modelos import Dulces, Mug

form = RifaForm

@app.route('/sorteo_dulces', methods=['GET', 'POST'])
def sorteo_dulces():
    form = RifaForm()

    if form.validate_on_submit():
        
        registrado = Dulces.query.filter_by(
            tel=form.tel.data).first()
        
        if registrado:

            flash('Usted ya se encuentra participando o ya participó del sorteo', 'error')

        else:

            nombre = form.nombre.data.title()
            tel = form.tel.data

            nuevo_usuario = Dulces(
                nombre = nombre,
                tel = tel
            )

            db.session.add(nuevo_usuario)
            db.session.commit()
            flash('Ahora estás agregado al sorteo', 'success')

        return render_template ('dulces.html', form=form)
    
    return render_template ('dulces.html', form=form)

@app.route('/sorteo_mug', methods=['GET', 'POST'])
def sorteo_mug():
    form = RifaForm()

    if form.validate_on_submit():

        flash('Ahora estás agregado al sorteo', 'success')
        return render_template ('mug.html', form=form)
    
    return render_template ('mug.html', form=form)

@app.route('/sortear', methods=['GET', 'POST'])
def sortear():

    usuarios = Dulces.query.filter(Dulces.elegible == 1).all()

    if usuarios:
        usuario_ganador = choice(usuarios)
        usuario_ganador.elegible = 2
        db.session.commit()
        flash(f'{usuario_ganador.nombre} ha ganado una bolsita de dulces. Avísale llamando al +57 {usuario_ganador.tel}', 'success')

    else:
        flash('No se encontraron usuarios disponibles para realizar el sorteo', 'error')
    return redirect (url_for('sorteo_dulces'))



