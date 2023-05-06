# -*- coding: utf-8 -*-
from django.urls import path

from .views import BreederResultsView


app_name = 'breeder'
urlpatterns = [
    path('results/', BreederResultsView.as_view(), name='results'),
]