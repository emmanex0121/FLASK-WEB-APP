from flask import Blueprint, render_template

views = Blueprint('views', __name__) # set up a blueprint for the flask app

@views.route('/') # define url to map to the route endpoint, in this case '/' - root, when we go to this root it calls the home function below
def home():
    return render_template('home.html')