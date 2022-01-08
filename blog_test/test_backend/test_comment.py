'''
Tests comment function defined in models.py.
'''

from blog.models import User, Post, register, post, comment


def test_user_requirements():
    '''
    Tests that only real users can comment on posts.
    '''
    real_user = register('realUser2', 'realUser2@test.ca', '#1abc', '#1abc')
    fake_user = User(
        username='fakeUser',
        email='fakeUser@test.ca',
        password='#1abc'
    )
    user_post = post(real_user, 'comments are cool', '')

    assert comment(real_user, user_post, 'this is a cool post') is not None
    assert comment(fake_user, user_post, 'this is a cool post') is None


def test_post_requirements():
    '''
    Tests that a user can only comment on a real post.
    '''
    user = register(
        'commentsOnPosts',
        'commentsOnPosts@test.ca',
        '#1abc',
        '#1abc'
    )

    real_post = post(user, 'a real post', '')
    fake_post = Post(
        username=user.username,
        title='A Real Post',
        content=''
    )

    assert comment(user, real_post, 'this was a real post') is not None
    assert comment(user, fake_post, 'this was a fake post') is None
