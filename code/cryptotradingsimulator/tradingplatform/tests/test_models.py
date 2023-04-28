from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.contrib import auth
from tradingplatform.models import Position, PlatformUser, CryptoCoin


class TestModels(TestCase):

    def create_crypto_coin(self):
        return CryptoCoin.objects.create(
            name="TestCoin",
            symbol="TST"
        )

    def test_crypto_coin_model(self):
        coin = self.create_crypto_coin()
        self.assertTrue(isinstance(coin, CryptoCoin))

    def create_platform_user(self):
        return PlatformUser.objects.create(
            user=User.objects.create_user(
                username='homer',
                password='simpson'
            )
        )

    def create_position(self):
        position = Position.objects.create(
            user=self.create_platform_user(),
            cryptocurrency=self.create_crypto_coin()
        )

        self.assertTrue(isinstance(position, Position))

    #def test_position_model(self):
    #    position = self.create_position()
    #    self.assertTrue(isinstance(position, Position))
