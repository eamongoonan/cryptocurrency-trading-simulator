from django.urls import path, include
from . import views
from django.contrib import admin

app_name = "tradingplatform"
urlpatterns = [
    path('', views.index, name='index'),  # /app
    path('trade', views.trade, name='trade'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('following', views.following, name='following'),
]
