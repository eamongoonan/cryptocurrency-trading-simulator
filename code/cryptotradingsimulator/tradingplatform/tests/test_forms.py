from django.test import TestCase, Client
from tradingplatform.forms import TradeForm
from django.urls import reverse
from django.contrib.auth.models import User
from django.db import models
import json


class TestViews(TestCase):

    def test_position_form(self):
        form = TradeForm(data={
            'cryptocurrency': 'BTC',
            'USD_value_of_purchase': 1000
        })

        #self.assertTrue(form.is_valid())

    def test_position_form_no_data(self):
        form = TradeForm(data={})

        self.assertFalse(form.is_valid())
