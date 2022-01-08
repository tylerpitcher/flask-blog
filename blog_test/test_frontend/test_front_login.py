from seleniumbase import BaseCase
from blog_test.conftest import base_url

import time


class FrontEndHomePageTest(BaseCase):

    def test_login_success(self, *_):
        self.open(base_url + '/signup')
        self.type('#email', 'frontLogin@test.ca')
        self.type('#username', 'frontLogin')
        self.type('#password1', '#1abc')
        self.type('#password2', '#1abc')
        self.click('input[type="submit"]')
        
        self.assert_element(".alert-success")

    def test_login_fail(self, *_):
        self.open(base_url + '/login')

        self.open(base_url + '/login')
        self.type('#email', 'noLogin@test.ca')
        self.type('#password', '#1abc')
        self.click('input[type="submit"]')

        self.assert_element(".alert-error")
