from django.db import models
from django.apps import AppConfig
from django.conf import settings
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import *


class CryptoCoin(models.Model):
    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=8)

    def __str__(self):
        return self.symbol


class PlatformUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.PositiveIntegerField(default=7000)
    ROI = models.FloatField(default=0)
    PNL = models.FloatField(default=0)

    def __str__(self):
        return str(self.user)


# Triggers instance of custom user model whenever a Django User is registered.
@ receiver(post_save, sender=User)
def create_platform_user(sender, instance, created, **kwargs):
    if created:
        PlatformUser.objects.create(user=instance)


class Position(models.Model):
    user = models.ForeignKey(PlatformUser, on_delete=models.PROTECT,)
    cryptocurrency = models.ForeignKey(CryptoCoin, on_delete=models.PROTECT, )
    USD_value_of_purchase = models.PositiveIntegerField('Purchase Value', default=0)
    current_coin_value = models.FloatField(blank=True, null=True)
    USD_value_of_sale = models.FloatField(blank=True, null=True)
    coin_amount = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    closed_at = models.DateTimeField(blank=True, null=True)
    ROI = models.FloatField(blank=True, null=True)
    PNL = models.FloatField(blank=True, null=True)
