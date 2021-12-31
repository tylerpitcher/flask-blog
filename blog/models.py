'''
Defines database models.
'''

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
import bcrypt

from blog.helpers import is_username, is_email, is_password, in_database
from blog import app

db = SQLAlchemy(app)


class User(db.Model):
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
    title = db.Column(db.String(32), unique=True)
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    comments = db.relationship('Comment')


class Comment(db.Model):
    '''
    Model that represents user's comments in the database.
    '''
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    msg = None


db.create_all()


def register(username, email, password):
    '''
    Creates new users & adds them to the database.
    Returns the new user if given valid input.
    '''
    if not is_username(username):
        return None
    users = User.query.filter_by(username=username).all()
    if len(users) != 0:
        return None
    if not is_password(password) or not is_email(email):
        return None
    users = User.query.filter_by(email=email).all()
    if len(users) != 0:
        return None

    user = User(
        username=username,
        email=email,
        password=bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
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
    if len(title) > 32 or len(title) < 3:
        return None

    post = Post(
        user_id=user.id,
        title=title.title(),
        content=content
    )

    db.session.add(post)
    db.session.commit()
    return post


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
        user_id=user.id,
        post_id=post.id,
        msg=msg
    )

    db.session.add(comment)
    db.session.commit()
    return comment
