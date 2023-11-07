from config import app
from log import login_manager
import control
import sign
import rutas
import perfil
import anuncios

login_manager.init_app(app)
login_manager.login_view = "login"

if __name__ == '__main__':
    app.run(debug=True)