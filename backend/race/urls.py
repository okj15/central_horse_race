# -*- coding: utf-8 -*-
from django.urls import path

from .views import RaceView

app_name = 'race'
urlpatterns = [
    path('', RaceView.as_view(), name='race list'),
]