from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = 'database.db'

def create_app():
    app = Flask(__name__) # creates the flask app
    # every flask app has the config variable used to
    # encrypt/secure session coookies related to the website
    app.config['SECRET_KEY'] = 'hehehe' # sets the SECRET_KEY
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    # The prefix '/' is to define everything in the
    # blue print path i.e views has routes 'buy' and 'jump'
    # we can easily access any of them /buy, /jump
    # but if a prefix is defined "/auth/" then you must
    # prefix all the routes to access them 
    # i.e /auth/buy, /auth/jump
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app