'''
Handles authentication routing.
'''

from flask import render_template, redirect, request, url_for, flash
from flask import Blueprint
from flask_login import login_required, login_user, logout_user, current_user

from blog.models import register, login, User

auth = Blueprint('auth', __name__)


@login_required
@auth.route('/logout')
def logout():
    '''
    Handles get request to logout user.
    '''
    logout_user()
    return redirect('/login')


@auth.route('/login')
def login_get():
    '''
    Handles get request for login page.
    '''
    if current_user.is_authenticated:
        return redirect(url_for('views.home'))
    return render_template('login.html', user=current_user)


@auth.route('/login', methods=['POST'])
def login_post():
    '''
    Handles post requests to login a user.
    '''
    if current_user.is_authenticated:
        return redirect(url_for('views.home'))

    user = login(
        request.form.get('email'),
        request.form.get('password')
    )

    if not user:
        flash('Login failed.', category='error')
        return render_template('login.html', user=current_user)

    login_user(user)
    flash('Login successful.', category='success')
    return redirect(url_for('views.home'))


@auth.route('/signup')
def sign_up_get():
    '''
    Handles sign up get requests.
    '''
    if current_user.is_authenticated:
        return redirect(url_for('views.home'))
    return render_template('signup.html', user=current_user)


@auth.route('/signup', methods=['POST'])
def sign_up_post():
    '''
    Handles post request to sign up a new user.
    '''
    if current_user.is_authenticated:
        return redirect(url_for('views.home'))

    user = register(
        request.form.get('username'),
        request.form.get('email'),
        request.form.get('password1'),
        request.form.get('password2')
    )

    if not isinstance(user, User):
        flash(user, category='error')
        return render_template('signup.html', user=current_user)

    login_user(user)
    flash('Sign-up successful.', category='success')
    return redirect(url_for('views.home'))
