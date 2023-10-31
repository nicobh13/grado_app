from flask import flash, redirect, render_template, url_for
from config import app
from log import login_required, logout_user

#Perfil de Usuario
@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/cerrar_sesion')
@login_required
def cerrar_sesion():
    logout_user()
    flash('Has cerrado sesión', 'success')
    return redirect (url_for('sign'))
