from django.test import SimpleTestCase
from django.urls import reverse, resolve
from members.views import login_user, logout_user, register_user


class TestURLs(SimpleTestCase):

    def test_login_url_resolves(self):
        url = reverse('members:login')
        self.assertEquals(resolve(url).func, login_user)

    def test_logout_url_resolves(self):
        url = reverse('members:logout')
        self.assertEquals(resolve(url).func, logout_user)

    def test_register_url_resolves(self):
        url = reverse('members:register')
        self.assertEquals(resolve(url).func, register_user)
