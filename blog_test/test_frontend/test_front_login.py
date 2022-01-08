from seleniumbase import BaseCase
from blog_test.conftest import base_url

# from blog.models import register


class FrontEndHomePageTest(BaseCase):

    def test_login_success(self, *_):
        # register('frontLogin', 'frontLogin@test.ca', '#1abc', '#1abc')

        self.open(base_url + '/login')
    #     self.type('#email', 'frontLogin@test.ca')
    #     self.type('#password', '#1abc')
    #     self.click('input[type="submit"]')

    #     self.assert_element(".alert-success")

    # def test_login_fail(self, *_):
    #     self.open(base_url + '/login')

    #     self.open(base_url + '/login')
    #     self.type('#email', 'noLogin@test.ca')
    #     self.type('#password', '#1abc')
    #     self.click('input[type="submit"]')

    #     self.assert_element(".alert-error")
