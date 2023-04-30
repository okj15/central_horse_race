# -*- coding: utf-8 -*-
from django.urls import path

from .views.race import RaceResultView, RaceInfoView

app_name = 'result'
urlpatterns = [
    path('raceinfo/', RaceInfoView.as_view(), name='race info'),
    path('races/', RaceResultView.as_view(), name='race list'),
]