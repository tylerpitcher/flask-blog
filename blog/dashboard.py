'''
Handles everything dashboard related on the backend.
'''

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
    posts = Post.query.filter_by(username=current_user.username).all()
    posts = sorted(
        posts,
        key=lambda p: len(p.comments), 
        reverse=True
    )

    popularPosts = getGraphData(posts)
    labels = [row[0] for row in popularPosts]
    data = [row[1] for row in popularPosts]

    posts = list(
        map(lambda p: (p, getPostPolarity(p)), posts)
    )
    
    return render_template(
        'dashboard.html', 
        user=current_user, 
        posts=posts, 
        labels=labels, 
        data=data
    )


def getCommentPolarity(comment):
    '''
    Gets polarity of a single comment.
    '''
    return TextBlob(comment.msg).sentiment.polarity


def getPostPolarity(post):
    '''
    Gets average polarity of comments in a post.
    '''
    if not len(post.comments):
        return 0

    polarities = list(map(getCommentPolarity, post.comments))
    sumOfPolarities = sum(polarities)
    
    if not sumOfPolarities:
        return 0

    return round(sumOfPolarities / len(polarities), 2)


def getGraphData(posts):
    '''
    Gets top 5 posts with most comments.
    '''
    if len(posts) > 5:
        posts = posts[0:6]

    return list(map(lambda p: (p.hash, len(p.comments)), posts))
