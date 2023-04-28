from django.test import SimpleTestCase
from django.urls import reverse, resolve
from tradingplatform.views import index, trade, portfolio, following


class TestURLs(SimpleTestCase):

    def test_index_url_resolves(self):
        url = reverse('tradingplatform:index')
        self.assertEquals(resolve(url).func, index)

    def test_trade_url_resolves(self):
        url = reverse('tradingplatform:trade')
        self.assertEquals(resolve(url).func, trade)

    def test_portfolio_url_resolves(self):
        url = reverse('tradingplatform:portfolio')
        self.assertEquals(resolve(url).func, portfolio)

    def test_following_url_resolves(self):
        url = reverse('tradingplatform:following')
        self.assertEquals(resolve(url).func, following)
