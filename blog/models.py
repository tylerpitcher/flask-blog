'''
Defines database models.
'''

from enum import unique
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from hashids import Hashids
import bcrypt

from blog.helpers import is_username, is_email, is_password, in_database
from blog import app

db = SQLAlchemy(app)


class User(db.Model, UserMixin):
    '''
    Model that represents users in the database.
    '''
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True)
    email = db.Column(db.String(320), unique=True)
    password = db.Column(db.String(60))
    posts = db.relationship('Post')
    comments = db.relationship('Comment')


class Post(db.Model):
    '''
    Model that represents user's posts in the database.
    '''
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    title = db.Column(db.String(64), unique=True)
    hash = db.Column(db.Text, unique=True)
    content = db.Column(db.Text)
    username = db.Column(db.String(32), db.ForeignKey('user.username'))
    comments = db.relationship('Comment', cascade="all, delete-orphan")


class Comment(db.Model):
    '''
    Model that represents user's comments in the database.
    '''
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    username = db.Column(db.String(32), db.ForeignKey('user.username'))
    post_hash = db.Column(db.Text, db.ForeignKey('post.hash'))
    hash = db.Column(db.Text, unique=True)
    msg = db.Column(db.Text)


db.create_all()


def register(username, email, password1, password2):
    '''
    Creates new users & adds them to the database.
    Returns the new user if given valid input.
    '''
    if not is_email(email):
        return 'Email not valid.'
    users = User.query.filter_by(email=email).all()
    if len(users) != 0:
        return 'Email already taken.'
    if not is_username(username):
        return 'Username not valid.'
    users = User.query.filter_by(username=username).all()
    if len(users) != 0:
        return 'Username already taken.'
    if not is_password(password1):
        return 'Password not valid.'
    if password1 != password2:
        return 'Passwords do not match.'

    user = User(
        username=username,
        email=email,
        password=bcrypt.hashpw(password1.encode('utf-8'), bcrypt.gensalt())
    )

    db.session.add(user)
    db.session.commit()
    return user


def login(email, password):
    '''
    Takes email & password to see if a user with those credentials
    exists in the database.
    Returns the user if they exist in the database.
    '''
    user = User.query.filter_by(email=email).first()
    if user is None:
        return None
    if not bcrypt.checkpw(password.encode('utf-8'), user.password):
        return None
    return user


def post(user, title, content):
    '''
    Creates a new post by user with given title & content.
    Returns the new post if given a valid title & content.
    '''
    if not in_database(User, user):
        return None
    if len(title) > 64 or len(title) < 3:
        return None

    existing_post = Post.query.filter_by(title=title.title()).first()
    if existing_post:
        return None

    new_post = Post(
        username=user.username,
        title=title.title(),
        content=content
    )

    db.session.add(new_post)
    db.session.commit()
    hashids = Hashids(min_length=5, salt=app.config['SECRET_KEY'])
    new_post.hash = hashids.encode(new_post.id) + 'P'
    db.session.commit()
    return new_post


def comment(user, post, msg):
    '''
    Creates comment by user on post.
    Returns the new comment if passed a real post and valid message.
    '''
    if not in_database(User, user) or not in_database(Post, post):
        return None
    if len(msg) < 2:
        return None

    comment = Comment(
        username=user.username,
        post_hash=post.hash,
        msg=msg
    )

    db.session.add(comment)
    db.session.commit()
    hashids = Hashids(min_length=5, salt=app.config['SECRET_KEY'])
    comment.hash = hashids.encode(comment.id) + 'C'
    db.session.commit()
    return comment


def delete(item):
    '''
    Delete entry in database table
    '''
    db.session.delete(item)
    db.session.commit()
