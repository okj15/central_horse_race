# -*- coding: utf-8 -*-
from django.urls import path

from .views.race import RaceView

app_name = 'result'
urlpatterns = [
    path('races/', RaceView.as_view(), name='race list'),
]