from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import auth
from django.db import models
import json


class TestViews(TestCase):

    def setUp(self):
        user = User.objects.create(username='homer')
        user.set_password('simpson')
        user.save()

    def test_login(self):
        login = self.client.login(username='homer', password='simpson')
        self.assertTrue(login)
