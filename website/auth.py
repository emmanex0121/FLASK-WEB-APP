from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__) # set up a blueprint for the flask app

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return render_template('logout.html')

@auth.route('/sign-up', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be greater than 3 chars', category='error')
        elif len(firstName) < 2:
            flash('Name must be greater than 1 char', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match', category='error')
        elif len(password1) < 7:
            flash('password must be at least 7 chars long', category='error')
        else:
            flash('Account created!', category='success')
    return render_template('sign_up.html')
