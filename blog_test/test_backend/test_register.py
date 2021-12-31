'''
Tests register function declared in models.py
'''

from blog.models import register


def test_username_requirements():
    '''
    Tests that only valid usernames can be used to register.
    '''
    assert register('UPPERCASE', 'uppercase@test.ca', '#1abc') is not None
    assert register('lowercase', 'lowercase@test.ca', '#1abc') is not None
    assert register('numbers123', 'numbers123@test.ca', '#1abc') is not None
    assert register('numbers1Mixed2In3', '1nums2@test.ca', '#1abc') is not None
    assert register('1numFirst', 'numFirst@test.ca', '#1abc') is None
    assert register('tooLong' * 10, 'tooLong@test.ca', '#1abc') is None
    assert register('slim', 'tooShort@test.ca', '#1abc') is None


def test_email_requirements():
    '''
    Tests that only valid rfc5322 emails can be used to register.
    '''
    assert register('validEmail', 'valid.email@test.ca', '#1abc') is not None
    assert register('dot', '.dot@test.ca', '#1abc') is None
    assert register('notAt', 'notAt.ca', '#1abc') is None


def test_password_requirements():
    '''
    Tests that only valid passwords can be used to register.
    '''
    assert register('validPassw', 'validPassw@test.ca', 'v#lid123') is not None
    assert register('longPwd', 'longPwd@test.ca', 'long' * 40) is None
    assert register('shortPassword', 'shortPassword@test.ca', '#1a') is None
    assert register('noSpeical', 'noSepcial@test.ca', '123ab') is None
    assert register('noNums', 'noNums@test.ca', '#abcd') is None
