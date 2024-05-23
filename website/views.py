from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint('views', __name__) # set up a blueprint for the flask app

@views.route('/') # define url to map to the route endpoint, in this case '/' - root, when we go to this root it calls the home function below
@login_required # cannot access home unless user is logged in
def home():
    return render_template('home.html')