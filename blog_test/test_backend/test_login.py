# '''
# Tests login function declared in models.py
# '''

# from blog.models import register, login


# def test_email_requirements():
#     '''
#     Tests that only emails in the database can be used.
#     '''
#     user = register('loginUser', 'loginUser@test.ca', '#1login', '#1login')
#     print(user)
#     assert login('loginUser@test.ca', '#1login') is user
#     assert login('wrongEmail@test.ca', '#login') is None


# def test_password_requirements():
#     '''
#     Tests that only a user's real password can be used.
#     '''
#     user = register('passUser', 'passUser@test.ca', '#1login', '#1login')
#     assert login('passUser@test.ca', '#1login') is user
#     assert login('passUser@test.ca', '#1wrong') is None
