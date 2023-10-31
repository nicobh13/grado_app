from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate


app=Flask(__name__)
app.secret_key = 'juli2201'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://nmora:nIcollemOra12@127.0.0.1:3306/tecnico'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
migrate = Migrate(app, db)
app.app_context().push()

