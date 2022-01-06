'''
Tests post function declared in models.py.
'''

from blog.models import User, register, post


def test_user_requirements():
    '''
    Tests that only a real user can post.
    '''
    real_user = register('realUser1', 'realUser1@test.ca', '#1abc')
    fake_user = User(
        username='fakeUser',
        email='fakeUser@test.ca',
        password='#1abc'
    )

    assert post(real_user, 'realUser', 'a real user') is not None
    assert post(fake_user, 'fakeUser', '') is None


def test_title_requirements():
    '''
    Tests that only valid titles can be used.
    '''
    user = register('poster', 'poster@test.ca', '#1abc')
    assert post(user, 'valid title', 'a valid title') is not None
    assert post(user, 'long' * 17, '') is None
    assert post(user, '', '') is None
