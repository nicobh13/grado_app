from config import app
from modelos import Usuario
from flask_login import LoginManager, login_user, login_required, logout_user, current_user


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_usuario(usuario_id):
    return Usuario.query.get(int(usuario_id))
