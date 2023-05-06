# -*- coding: utf-8 -*-
from django.urls import path

from .views import OwnerResultsView


app_name = 'owner'
urlpatterns = [
    path('results/', OwnerResultsView.as_view(), name='results'),
]