from flask import Flask

def create_app():
    app = Flask(__name__) # creates the flask app
    # every flask app has the config variable used to
    # encrypt/secure session coookies related to the website
    app.config['SECRET_KEY'] = 'hehehe' # sets the SECRET_KEY

    return app