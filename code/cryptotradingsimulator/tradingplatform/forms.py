from django import forms
from django.forms import ModelForm
from .models import Position
from .live_coin_price import get_coin_price


class TradeForm(ModelForm):

    class Meta:
        model = Position
        fields = ('cryptocurrency', 'USD_value_of_purchase')


class SellForm(ModelForm):

    class Meta:
        model = Position
        fields = ()
