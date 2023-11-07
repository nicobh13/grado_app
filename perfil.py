from flask import flash, redirect, render_template, url_for
from config import app
from log import login_required, logout_user, login_manager, current_user


#Perfil de Usuario
@app.route('/dashboard')
@login_required
def dashboard():
    if current_user.is_authenticated:
        id = current_user.id
        return render_template ('dashboard.html', id=id)
    else:
        return redirect (url_for('sign'))
    
@app.route('/cerrar_sesion')
@login_required
def cerrar_sesion():
    logout_user()
    flash('Has cerrado sesión', 'warning')
    return redirect (url_for('sign'))

