# -*- coding: utf-8 -*-
from django.urls import path

from .views import JockeyResultsView


app_name = 'jockey'
urlpatterns = [
    path('results/', JockeyResultsView.as_view(), name='results'),
]