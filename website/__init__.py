from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

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

    # Check if the database exists before we start the app
    from .models import User, Note
    with app.app_context():
        create_database()
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login' # redirect to auth.login if user is not logged in where there is a @loginrequired
    login_manager.init_app(app)

    # Telling flask how we load a user
    # Telling flask what user we are looking for
    # looking for user model and we gonna refeence them by their id
    # and the DECORATOR is saying use the load_user function to load user
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_database():
    """
        Creates Database if it doesnt exists
    """
    if not path.exists('website/' + DB_NAME):
        db.create_all()
        print('Created Database!')