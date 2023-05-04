# -*- coding: utf-8 -*-
from django.urls import path

from .views.list import RacingHorseResultsView
from .views.detail import RacingHorseDetailView

app_name = 'racing_horse'
urlpatterns = [
    path('results/', RacingHorseResultsView.as_view(), name='race list'),
    path('detail/<int:pk>/', RacingHorseDetailView.as_view(), name='race list'),
]