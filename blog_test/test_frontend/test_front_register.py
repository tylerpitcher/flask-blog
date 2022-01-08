from seleniumbase import BaseCase
from blog_test.conftest import base_url


class FrontEndHomePageTest(BaseCase):

    def test_register_success(self, *_):
        self.open(base_url + '/signup')
        self.type('#email', 'frontSignup@test.ca')
        self.type('#username', 'frontRegister')
        self.type('#password1', '#1abc')
        self.type('#password2', '#1abc')
        self.click('input[type="submit"]')

        self.assert_element(".alert-success")

    def test_register_fail(self, *_):
        self.open(base_url + '/signup')
        self.type('#email', 'noSignup@test.ca')
        self.type('#username', 'no')
        self.type('#password1', 'no')
        self.type('#password2', 'no')
        self.click('input[type="submit"]')

        self.assert_element(".alert-error")
