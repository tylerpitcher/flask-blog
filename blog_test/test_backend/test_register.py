# '''
# Tests register function declared in models.py
# '''

# from blog.models import register, User


# def test_username_requirements():
#     '''
#     Tests that only valid usernames can be used to register.
#     '''
#     assert isinstance(
#         register('UPPERCASE', 'uppercase@test.ca', '#1abc', '#1abc'), User)
#     assert isinstance(
#         register('lowercase', 'lowercase@test.ca', '#1abc', '#1abc'), User)
#     assert isinstance(
#         register('numbers123', 'numbers123@test.ca', '#1abc', '#1abc'), User)
#     assert isinstance(register(
#         'numbers1Mixed2In3', '1nums2@test.ca', '#1abc', '#1abc'), User)
#     assert not isinstance(
#         register('1numFirst', 'numFirst@test.ca', '#1abc', '#1abc'), User)
#     assert not isinstance(
#         register('tooLong' * 10, 'tooLong@test.ca', '#1abc', '#1abc'), User)
#     assert not isinstance(
#         register('slim', 'tooShort@test.ca', '#1abc', '#1abc'), User)


# def test_email_requirements():
#     '''
#     Tests that only valid rfc5322 emails can be used to register.
#     '''
#     assert isinstance(
#         register('validEmail', 'valid.email@test.ca', '#1abc', '#1abc'), User)
#     assert not isinstance(
#         register('dot', '.dot@test.ca', '#1abc', '#1abc'), User)
#     assert not isinstance(
#         register('notAt', 'notAt.ca', '#1abc', '#1abc'), User)


# def test_password_requirements():
#     '''
#     Tests that only valid passwords can be used to register.
#     '''
#     assert isinstance(register(
#         'validPassw', 'validPassw@test.ca', 'v#lid123', 'v#lid123'), User)
#     assert not isinstance(
#         register('longPwd', 'longPwd@test.ca', 'long' * 40, 'long' * 40), User)
#     assert not isinstance(
#         register('shortPassword', 'shortPassword@test.ca', '#1a', '#1a'), User)
#     assert not isinstance(
#         register('noSpeical', 'noSepcial@test.ca', '123ab', '123ab'), User)
#     assert not isinstance(
#         register('noNums', 'noNums@test.ca', '#abcd', '#abcd'), User)
