'''
Handles main routing requests.
'''

from flask import redirect, render_template, request, url_for, jsonify
from flask import Blueprint, flash
from flask_login import current_user, login_required

from blog.models import Post, Comment, comment, post, delete

views = Blueprint('views', __name__)


@views.route('/')
def home():
    '''
    Handles get requests for index page.
    '''
    if current_user.is_authenticated:
        posts = Post.query.filter(Post.username != current_user.username)
    else:
        posts = Post.query.all()
    return render_template('index.html', user=current_user, posts=posts)


@views.route('/create')
@login_required
def create_get():
    '''
    Handles get requests for create post page.
    '''
    return render_template('create.html')


@views.route('/create', methods=['POST'])
@login_required
def create_post():
    '''
    Handles post requests to create a new product.
    '''
    title = request.form.get('title')
    content = request.form.get('content')

    new_post = post(
        current_user,
        title=title,
        content=content
    )

    if not new_post:
        flash('Post not created.', category='error')
        return render_template('create.html')
    return redirect(url_for('views.profile_get'))


@views.route('/post/<hash>')
def show_post_get(hash):
    '''
    Handles get requests for a certain post.
    '''
    current_post = Post.query.filter_by(hash=hash).first()
    if not current_post:
        return redirect(url_for('views.home'))
    return render_template('post.html', user=current_user, post=current_post)


@views.route('/post/<hash>', methods=['POST'])
def show_post_post(hash):
    '''
    Handles post requests for a post's page to create comments.
    '''
    current_post = Post.query.filter_by(hash=hash).first()
    if not current_post:
        return redirect(url_for('views.home'))
    if not current_user.is_authenticated:
        flash('Must login to comment.', category='error')
        return render_template(
            'post.html',
            user=current_user,
            post=current_post
        )

    msg = request.form.get('comment')
    comment(
        current_user,
        current_post,
        msg
    )

    return render_template('post.html', user=current_user, post=current_post)


@views.route('/profile')
@login_required
def profile_get():
    '''
    Handles get requests for profile page.
    '''
    posts = Post.query.filter_by(username=current_user.username)
    return render_template('profile.html', user=current_user, posts=posts)


@views.route('/remove', methods=['DELETE'])
@login_required
def remove():
    '''
    Handles post requests to remove comments or posts.
    '''
    hash = request.form['hash']
    item = None
    if hash[-1] == 'C':
        item = Comment.query.filter_by(hash=hash).first()
    elif hash[-1] == 'P':
        item = Post.query.filter_by(hash=hash).first()

    if item and item.username == current_user.username:
        delete(item)

    return jsonify({})
