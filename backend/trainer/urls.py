# -*- coding: utf-8 -*-
from django.urls import path

from .views import TrainerResultsView


app_name = 'trainer'
urlpatterns = [
    path('results/', TrainerResultsView.as_view(), name='results'),
]