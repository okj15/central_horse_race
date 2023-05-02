# -*- coding: utf-8 -*-
from django.urls import path

from .views.result import RacingHorseResultsView

app_name = 'racing_horse'
urlpatterns = [
    path('results/', RacingHorseResultsView.as_view(), name='race list'),
]