from django.urls import path

# from . import views
from .views import home, matome

urlpatterns = [
    path('', home.index, name='index'),
    path('matome', matome.index, name='index'),
]