from django.test import TestCase, Client
from django.urls import reverse
from tradingplatform.forms import TradeForm
from django.contrib.auth.models import User
from tradingplatform.models import Position, PlatformUser, CryptoCoin
from django.db import models
import json


class TestViews(TestCase):

    def test_user_logs_in_creates_position(self):
        test_user = User.objects.create(username='testuser10')
        test_user.set_password('secret')
        test_user.id = 1000
        test_user.save()

        coin = CryptoCoin.objects.create(
            name="TestCoin",
            symbol="TST"
        )

        platform_user = PlatformUser.objects.create(user=test_user)

        login = self.client.login(username='testuser10', password='secret')
        self.assertTrue(login)

        position = Position.objects.create(
            user=platform_user,
            cryptocurrency=coin
        )

        self.assertTrue(isinstance(position, Position))
