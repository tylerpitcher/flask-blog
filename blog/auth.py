from flask import Blueprint, render_template, redirect, request, jsonify, \
                  url_for
from flask_login import login_required, login_user, logout_user, current_user

from blog.models import register, login
from blog.helpers import is_email, is_username, is_password

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
        return render_template('login.html', user=current_user)

    login_user(user)
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
        request.form.get('password1')
    )

    if not user:
        return render_template('signup.html', user=current_user)

    login_user(user)
    return redirect(url_for('views.home'))


@auth.route('/signup/verify', methods=['POST'])
def verify_post():
    '''
    Handles post requests to verify input.
    '''
    if current_user.is_authenticated:
        return redirect(url_for('views.home'))

    valid_email = is_email(request.form['email'])
    valid_username = is_username(request.form['username'])
    valid_password1 = is_password(request.form['password1'])
    match = request.form['password1'] == request.form['password1']

    return jsonify({
        'email': valid_email,
        'username': valid_username,
        'password1': valid_password1,
        'passwords_match': match
    })
