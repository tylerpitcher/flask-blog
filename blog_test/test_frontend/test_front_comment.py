# from seleniumbase import BaseCase
# from blog_test.conftest import base_url

# from blog.models import register, post


# class FrontEndHomePageTest(BaseCase):

#     def test_comment_success(self, *_):
#         u = register('frontComment', 'frontComment@test.ca', '#1abc', '#1abc')
#         post(u, 'Comment Here', '')

#         self.open(base_url + '/login')
#         self.type('#email', 'frontComment@test.ca')
#         self.type('#password', '#1abc')
#         self.click('input[type="submit"]')

#         self.open(base_url + '/profile')
#         self.click('.posts .snippet a')

#         self.type('input[type="text"]', 'my comment')
#         self.click('input[type="submit"]')

#         self.assert_element('.comments .content')

#     def test_comment_fail(self, *_):
#         u = register('noComment', 'noComment@test.ca', '#1abc', '#1abc')
#         post(u, 'No Comment', '')

#         self.open(base_url)
#         self.click('.posts .snippet')

#         self.type('input[type="text"]', 'my comment')
#         self.click('input[type="submit"]')

#         self.assert_element('.alert-error')
