from flask import render_template
from flask import Blueprint
from flask_login import current_user, login_required
from textblob import TextBlob

from blog.models import Post

dashboard = Blueprint('dashboard', __name__)


@dashboard.route('/')
@login_required
def dashboard_get():
    '''
    Handles get requests for dashboard page.
    '''
    posts = Post.query.all()
    posts = sorted(
        posts,
        key=lambda p: len(p.comments), 
        reverse=True
    )
    posts = list(
        map(lambda p: (p, getPostPolarity(p)), posts)
    )

    return render_template('dashboard.html', user=current_user, posts=posts)


def getCommentPolarity(comment):
    return TextBlob(comment.msg).sentiment.polarity


def getPostPolarity(post):
    if not len(post.comments):
        return 0

    polarities = list(map(getCommentPolarity, post.comments))
    sumOfPolarities = sum(polarities)
    
    if not sumOfPolarities:
        return 0

    return round(sumOfPolarities/len(polarities), 2)
