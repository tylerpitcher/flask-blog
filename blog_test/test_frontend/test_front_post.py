'''
Frontend tests for posting content.
'''
from seleniumbase import BaseCase
from blog_test.conftest import base_url

from blog.models import register


class FrontEndHomePageTest(BaseCase):

    def test_post_success(self, *_):
        register('frontPoster1', 'frontPoster1@test.ca', '#1abc', '#1abc')

        self.open(base_url + '/login')
        self.type('#email', 'frontPoster1@test.ca')
        self.type('#password', '#1abc')
        self.click('input[type="submit"]')

        self.open(base_url + '/create')
        self.type('#title', 'Successful post')
        self.click('input[type="submit"]')

        self.open(base_url + '/dashboard')
        self.assert_element('.posts .content')

    def test_post_fail(self, *_):
        register('frontPoster2', 'frontPoster2@test.ca', '#1abc', '#1abc')

        self.open(base_url + '/login')
        self.type('#email', 'frontPoster2@test.ca')
        self.type('#password', '#1abc')
        self.click('input[type="submit"]')

        self.open(base_url + '/create')
        self.type('#title', 'no')
        self.click('input[type="submit"]')

        self.assert_element('.alert-error')
